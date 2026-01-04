from django.urls import path
from .views import (
    NaturalPersonListView,
    NaturalPersonCreateView,
    NaturalPersonDetailView,
    NaturalPersonUpdateView,
    LoginView,
    LogoffView
)
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', NaturalPersonListView.as_view(), name='natural_person-list'),
    path('create/', NaturalPersonCreateView.as_view(), name='natural_person-create'),
    path('details/<int:pk>/', NaturalPersonDetailView.as_view(), name='natural_person-details'),
    path('edit/<int:pk>/', NaturalPersonUpdateView.as_view(), name='natural_person-edit'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoffView.as_view(), name='logout')
] 
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
