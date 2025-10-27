from django.urls import path, include
from . import views
from appadv import views

from .views import PersonListView, PersonFormView

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('json/', views.show_json_data, name='show_json_data'),
    path('google/', views.redirect_google, name='redirect_google'),
    path('fill/', views.fill_database, name='fill_database'),
    path('people/', PersonListView.as_view(), name='person_list_view'),
    path('create/', PersonFormView.as_view(), name='person_form_view'),
]
