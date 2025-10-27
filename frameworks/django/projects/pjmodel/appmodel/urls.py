from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fill/', views.fill, name='fill'),
    path('clear/', views.clear, name='clear'),
    path('create/', views.create, name='create'),
    path('get_person_by_nae/<str:name>', views.get_person_by_name, name='get_person_by_name'),
    path('get_person_by_id/<int:id>', views.get_person_by_id, name='get_person_by_id'),
    path('delete/<int:id>', views.delete, name='delete'),
]
