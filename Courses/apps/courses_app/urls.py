from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^destroy/(?P<urlID>\d+)$', views.destroy),
    url(r'^add$', views.add),
    url(r'^delete/(?P<urlID>\d+)$', views.delete),
]
