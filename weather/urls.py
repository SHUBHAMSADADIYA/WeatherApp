from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('tenDaysDetail', views.tenDaysDetail, name='tenDaysDetail'),
    path('news', views.news, name='news'),
    path('newsDetail', views.newsDetail, name='newsDetail'),
    path('hourly', views.hourly_view, name='hourly'),
]
