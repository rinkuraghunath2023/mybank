from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [

    path('',views.demo,name='demo'),
    path('newpage',views.newpage,name='newpage'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('forms',views.forms,name='forms'),
    path('lastpage',views.lastpage,name='lastpage'),
    path('get_cities/',views.get_cities,name='get_cities'),

]
