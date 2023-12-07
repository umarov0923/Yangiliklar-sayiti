from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import News
from .forms import ContactForm

# Create your views here.

def news_item(request,news):
    new = get_object_or_404(News,slug=news, status=News.Status.Published)

    context = {
        "new":new
    }

    return render(request,'news/new_item.html', context=context)

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