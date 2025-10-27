from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('condition/', views.condition, name='condition'),
    path('looping/', views.looping, name='looping'),
    path('greeting/', views.greeting, name='greeting'),
    path('json/', views.json, name='json'),
    path('redirect_to_google/', views.redirect_to_google, name='redirect_to_google'),
    path('register/', views.register, name='register'),
    path('delete/<int:_id>', views.delete, name='delete'),
    path('details/<int:_id>', views.details, name='details'),
]
