from django.urls import path
from .views import news_item, HomepegeList, contactPageView,MahaliyListView,TexnolListView,XorijListView,SportlListView,SiyosatlListView

urlpatterns = [
    path('news/<slug:news>/',news_item, name='new_item'),
    path('', HomepegeList.as_view(), name= 'index'),
    path('contact/',contactPageView, name='contact'),
    path('mahaliy/',MahaliyListView.as_view(), name='mahaliy_f'),
    path('texhologiya/', TexnolListView.as_view(), name="texnologiya_f"),
    path('xorij/', XorijListView.as_view(),name='xorij_f'),
    path('sport/',SportlListView.as_view(), name="sport_f"),
    path("siyosat/", SiyosatlListView.as_view(), name='siyosat_f')
]