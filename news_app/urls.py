from django.urls import path
from .views import  NewsItemView, HomepegeList, contactPageView,MahaliyListView,TexnolListView,XorijListView,SportlListView,SiyosatlListView, \
    NewsUpdateView, NewsDeleteView, admin_page, SearchResultsView

urlpatterns = [
    # path('news/<slug:news>/',news_item, name='new_item'),
    path("news/<slug:news>/", NewsItemView.as_view(), name='new_item'),
    path('', HomepegeList.as_view(), name= 'index'),
    path('contact/',contactPageView, name='contact'),
    path('mahaliy/',MahaliyListView.as_view(), name='mahaliy_f'),
    path('texhologiya/', TexnolListView.as_view(), name="texnologiya_f"),
    path('xorij/', XorijListView.as_view(),name='xorij_f'),
    path('sport/',SportlListView.as_view(), name="sport_f"),
    path("siyosat/", SiyosatlListView.as_view(), name='siyosat_f'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='new_update'),
    path('news/<slug>/delet/', NewsDeleteView.as_view(), name='new_delet'),
    path("admin_page/", admin_page, name="admin_page"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
]