from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^users/(?P<userID>\d+)$', views.displayUser),
    url(r'^logout$', views.logout, name='logout'),
]
