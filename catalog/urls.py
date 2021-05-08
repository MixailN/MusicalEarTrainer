from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.catalog, name='catalog'),
    url(r'^(\d+)/$', views.get_exercise),
    url(r'^task/$', views.get_task),
]