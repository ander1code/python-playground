from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls import handler404, handler403
from datetime import datetime

from django.conf.urls.static import static
from django.conf import settings

extra_urlpatterns = [
    path('hello/', views.index, name='index'),
]

write_views_urlpatterns = [
    path('1/', views.show_sample_view, name='show_sample_view', kwargs={'current_time':datetime.strftime(datetime.today(), '%m/%d/%Y - %H:%M:%S')}),
    # path('4/', views.current_datetime, name='current_datetime'),
    path('2/<str:name>', views.find_person_in_people_by_name, name='find_person_in_people_by_name'),
    path('3/<int:id>', views.get_person_by_id, name='get_person_by_id'),
    path('5/', views.execute_post, name='execute_post'),
    path('6/', views.upload_file, name='upload_file'),
    path('7/', views.ViewWithDecorator.as_view(), name='view_with_decorator'),
    path('8/<int:id>', views.get_person_details_01, name='get_person_details_01'),
    path('9/<int:id>', views.get_person_details_02, name='get_person_details_02'),
]


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^cep/(?P<cep>\d{5}-?\d{3})/$', views.search_cep),
    path('greeting/<str:name>', include(extra_urlpatterns)),
    path('checkage', include([
            path('/<int:age>', views.check_age, name='check_age')
        ])
    ),
    path('greeting_to_html/<str:name>', views.greeting_to_html, name='greeting_to_html'),
    path('iteration/', views.execute_list_iteration, name='list_iteration'),
    # path('greeting_redirect/<str:name>', views.greeting_redirect),
    path('write_view/', include(write_views_urlpatterns)),
]

handler404 = views.error_404
handler403 = views.error_403
