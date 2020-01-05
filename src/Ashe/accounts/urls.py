from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name="homepage"),
    path('', views.homepage, name='homepage'),
    path('login_page', views.login_page, name="homepage"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
    path('send_image', views.send_image, name="send_image"),
    path('post_comments', views.post_comments, name="post_comments"),
]