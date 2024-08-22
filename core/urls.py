from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('download_video/', views.download_video, name='download_video'),
    path('features/', views.features, name="features"),
    path('pricing/', views.pricing, name="pricing"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_register/', views.user_register, name="user_register"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('yt_audio/', views.yt_audio, name="yt_audio"),
    path('yt_shorts/', views.yt_shorts, name="yt_shorts"),
    path('yt_playlist/', views.yt_playlist, name="yt_playlist"),
    path('yt_subtitle/', views.yt_subtitle, name="yt_subtitle"),
    path('yt_thumbnail/', views.yt_thumbnail, name="yt_thumbnail"),
]