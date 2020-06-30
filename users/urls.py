# -*- coding: utf-8 -*-
from django.urls import path, include
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


app_name='users'

urlpatterns=[
    #path('',include('django.contrib.auth.urls')),
    path('admin/',admin.site.urls),
    path('login/',views.loginfn,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutUser,name='logout'), 
    ]

