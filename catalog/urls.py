from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.catalog, name='catalog'),
    url(r'^(\d+)/$', views.get_exercise),
]