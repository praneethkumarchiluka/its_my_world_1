# -*- coding: utf-8 -*-
from django.urls import path
from django.contrib import admin  
from . import views

app_name='tester'
urlpatterns = [
    path('admin/',admin.site.urls),  
    path('', views.home,name='home'),
    path('details/',views.details,name='details'),
    path('base/',views.base,name='base'),
    path('adddetails/',views.adddetails,name='adddetails'),
    path('profile/',views.profile,name='profile'),
    path('sudo',views.sudo,name='sudo'),
    path('sudo1',views.sudo1,name='sudo1'),
    path('homesudo',views.homesudo,name='homesudo'),
    path('success1',views.success1,name='success1'),
    path('uprofile',views.uprofile,name='uprofile'),
    path('exam/',views.exam,name='exam'),
    path('about',views.about,name='about'),
    path('story/<int:id>',views.story,name='story'),
    path('remove/<int:id>',views.delete,name='remove'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('viewprofiles',views.viewprofile,name='viewprofiles'),
    path('sudohome',views.sudohome,name='sudohome'),
    path('happiness',views.happiness,name='happiness'),
    path('motivation',views.motivation,name='motivation'),
    path('relaxing',views.relaxing,name='relaxing'),
    path('music',views.music,name='music'),
    path('dele',views.dele,name='dele'),

    path('password-reset',views.change,name='forgot'),

]