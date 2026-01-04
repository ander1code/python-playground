from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.list, name="natural_person-list"),
    path('create/', views.create, name="natural_person-create"),
    path('details/<int:id>/', views.details, name="natural_person-details"),
    path('edit/<int:id>/', views.edit, name="natural_person-edit"),
    path('login/', views.login_auth, name='login'),
    path('logout/', views.logoff_auth, name='logout')
] 
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
