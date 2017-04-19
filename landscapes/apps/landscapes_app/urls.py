from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>[1-9]|[1-4][0-9]|[5][0])$', views.process)
]