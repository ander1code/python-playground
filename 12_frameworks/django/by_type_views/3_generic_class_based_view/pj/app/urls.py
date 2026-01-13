from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    LoginView, 
    LogoutView, 
    NaturalPersonListView, 
    NaturalPersonCreateView, 
    NaturalPersonUpdateView, 
    NaturalPersonDetailView
)

urlpatterns = [
    path('', NaturalPersonListView.as_view(), name='natural_person_list'),
    path('create/', NaturalPersonCreateView.as_view(), name='natural_person_create'),
    path('edit/<int:pk>/', NaturalPersonUpdateView.as_view(), name='natural_person_edit'),
    path('details/<int:pk>/', NaturalPersonDetailView.as_view(), name='natural_person_details'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
