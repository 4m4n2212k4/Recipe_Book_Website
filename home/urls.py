from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.loginUser,name="login"),
    path("login",views.loginUser,name="login"),
    path("logout",views.logoutUser,name="logout"),
    path("home",views.index,name="home"),
    path("about",views.about,name='about'),
    path("blog",views.blog,name='blog'),
    path("contact",views.contact,name='contact'),
    path("menu",views.menu,name='menu'),
    # path("services",views.services,name='services'),
    
]