from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm,UserRegistrationForm, UserEditForm , ProfileEditForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Profile

def user_login(request):
    if request.method =="Post":
        form = LoginForm(request.Post)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username = data["username"],
                                password = data['password'])
            if user is not None:
                if user.is_active():
                    login(request, user)
                    return HttpResponse("Muvaffaqiyatli login amalga oshirildi")
                else:
                    return HttpResponse("Sizning profilingiz faol  holatda emas")
            else:
                return HttpResponse("Login va parolda xatolik bor")
    else:
        form = LoginForm()
        context = {
            'from':form
        }
    return render(request, "registration/login.html", context)

def user_profile(request):
    user = request.user
    profil_info = Profile.objects.get(user=user)
    context = {
        "user":user,
        "profile":profil_info
    }

    return render(request,"pages/user_profile.html", context)

def user_register(request):
    if request.method=="POST":
        user_form= UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user= user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {
                "new_user":new_user
            }

            return render(request,"account/register_done.html",context)
    else:
        user_form = UserRegistrationForm()
        context = {
            "user_form": user_form
        }
        return render(request,"account/register.html", context)

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "account/register.html"
@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('login')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        context = {
        "user_form":user_form,
        "profile":profile_form
        }

        return render(request, "account/profile_edit.html", context)