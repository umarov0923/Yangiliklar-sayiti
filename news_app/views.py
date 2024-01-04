from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from hitcount.views import HitCountDetailView


from .models import News
from .forms import ContactForm, CommentForm
from news_app.custom_permissions import OnlyLoggedSuperUser

class SearchResultsView(ListView):
    model = News
    template_name = "news/search_results.html"
    context_object_name = 'search_result'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        search_list = News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return search_list

# @login_required
# def news_item(request,news):
#     new = get_object_or_404(News,slug=news, status=News.Status.Published)
#     comments = new.comments.filter(active=True)
#     if request.method=='POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.news = new
#             new_comment.user = request.user
#             new_comment.save()
#             comment_form = CommentForm()
#     else:
#         comment_form = CommentForm()
#
#     context = {
#         "new":new,
#         'comments':comments,
#         'comment_form':comment_form
#     }
#
#     return render(request,'news/new_item.html', context=context)
class NewsItemView(HitCountDetailView, DetailView):
    model = News
    template_name = 'news/new_item.html'
    context_object_name = 'new'
    slug_field = 'slug'
    slug_url_kwarg = 'news'
    count_hit = True  # Указывает, что нужно увеличивать счетчик


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        context['comment_form'] = CommentForm()
        context['comment_count'] = self.object.comments.filter(active=True).count()

        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = self.object
            new_comment.user = request.user
            new_comment.save()
        return self.render_to_response(self.get_context_data(comment_form=comment_form))


# def home(request):
#     categories = Category.objects.all()
#     new_list = News.published.all().order_by('-publish_time')[:5]
#     mahaliy_news = News.published.filter(category__name="mahaliy")[1:6]
#     mahaliy_ones = News.published.filter(category__name="mahaliy")[:1]
#     xorij= News.published.filter()
#
#
#     context = {
#         'new_list':new_list,
#         'categories':categories,
#         "mahaliy_news":mahaliy_news,
#         "mahaliy_ones":mahaliy_ones
#     }
#
#     return render(request,'news/index.html', context)

def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("<h2> Biz bilan boglanganiz uchun raxmat!")

    context = {
        'form':form
    }

    return render(request,'news/contact.html', context)

class HomepegeList(ListView):
    model = News
    template_name = "news/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_list"] = News.published.all().order_by('-publish_time')[:5]
        context["mahaliy_news"] = News.published.filter(category__name="mahaliy").order_by('-publish_time')[:6]
        context["xorij_news"] = News.published.filter(category__name="xorijiy").order_by('-publish_time')[:5]
        context["texnologiya_news"] = News.published.filter(category__name="texnologiya").order_by('-publish_time')[:5]
        context["sport_news"] = News.published.filter(category__name="sport").order_by('-publish_time')[:5]
        return context


class MahaliyListView(ListView):
    model = News
    template_name = "news/mahaliy.html"
    context_object_name = 'mahaliy_yangiliklar'

    def get_queryset(self):
        news= self.model.published.all().filter(category__name="mahaliy")

        return news


class XorijListView(ListView):
    model = News
    template_name = "news/xorij.html"
    context_object_name = 'xorij_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="xorijiy")

        return news


class TexnolListView(ListView):
    model = News
    template_name = "news/texnol.html"
    context_object_name = 'texnologiya_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="texnologiya")

        return news

class SportlListView(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="sport")

        return news

class SiyosatlListView(ListView):
    model = News
    template_name = "news/siyosat.html"
    context_object_name = 'siyosiy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Siyosat")

        return news

class NewsUpdateView(OnlyLoggedSuperUser,UpdateView):
    model = News
    fields = ('title','body','category','status','image')
    template_name = 'crud/news_edit.html'
    success_url = reverse_lazy("index")

class NewsDeleteView(OnlyLoggedSuperUser,DeleteView):
    model = News
    template_name = 'crud/news_delet.html'
    success_url = reverse_lazy("index")
@login_required
@user_passes_test(lambda u:u.is_superuser)
def admin_page(request):
    admin_users = User.objects.filter(is_superuser=True)

    context = {
        "admin_users":admin_users
    }

    return render(request,"pages/admin_page.html", context)