from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import Example02TemplateView, PersonListView, PersonDirectDeleteView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('template_view_01/', TemplateView.as_view(template_name="contents/template_view.html", extra_context={'message':'Hello, World!'} ), name='template_view_01'),
    path('template_view_02/', Example02TemplateView.as_view(), name="Example02TemplateView"),
    path('person/', PersonListView.as_view(), name="PersonListView"),
    path('person/delete/<int:pk>', PersonDirectDeleteView.as_view(), name="PersonDirectDeleteView"),
]
