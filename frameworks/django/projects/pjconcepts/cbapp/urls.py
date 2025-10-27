from django.urls import path, reverse_lazy, include
from . import views

crud_urlpatterns  = [
    path('', views.PersonIndex.as_view(), name='person-index'),
    path('males/', views.PersonMaleIndex.as_view(), name='person-male-index'),
    path('create/', views.PersonCreateFormView.as_view(), name='person-create-form'),
    path('details/<int:pk>', views.PersonDetail.as_view(), name='person-details'),
    path('update/<int:pk>', views.PersonUpdateView.as_view(), name='person-update'),
]

urlpatterns = [
    path('', views.HelloWorldTemplateView.as_view()),
    path('2/', views.HelloWorldTemplateView.as_view(template_name='contents/hello2.html', extra_context={'message':'Olá, Mundo!'})),
    path('3/', views.MyRedirectView.as_view(), name='redirect-to-youtube'),
    path('4/', views.MyRedirectView.as_view(url=reverse_lazy('to_redirect'), permanent=True), name='redirect'),
    path('redirection/', views.to_redirect, name='to_redirect'),
    path('crud/', include(crud_urlpatterns))
]