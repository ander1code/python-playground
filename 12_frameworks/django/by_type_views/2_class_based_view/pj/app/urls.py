from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    ListView,
    CreateView,
    DetailsView,
    EditView,
    LogoutView,
    LoginView
)

urlpatterns = [
    path('', ListView.as_view(), name="natural_person-list"),
    path('create/', CreateView.as_view(), name="natural_person-create"),
    path('details/<int:id>/', DetailsView.as_view(), name="natural_person-details"),
    path('edit/<int:id>/', EditView.as_view(), name="natural_person-edit"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
] 
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
