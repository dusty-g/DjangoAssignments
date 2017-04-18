from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show$', views.show),
    url(r'^create$', views.create)
]
