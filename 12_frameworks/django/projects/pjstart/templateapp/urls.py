"""
URL configuration for pjstart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_test/', views.view_test, name='view_test'),
    path('hello1/', TemplateView.as_view(template_name='contents/hello1.html')),
    path('hello2/', views.MyTemplateView.as_view(), name='hello2'),
    path('hello3/', views.AsyncView.as_view(), name='hello3'),
    path('hello4/', views.HelloWorldView.as_view(), name='hello4'),
    path('hello5/', views.HelloWorldView.as_view(message='Olá, Mundo!'), name='hello5'),
    path('translate/', views.translate_page, name='translate'),
]
