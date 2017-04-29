from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.secrets, name='new'),
    url(r'^add$', views.add, name='add'),
    url(r'^delete/$', views.secrets, name='delete'),
    url(r'^delete/(?P<ID>\d*)/(?P<page>\w*)$', views.delete),
    url(r'^like/$', views.secrets, name='like'),
    url(r'^popular$', views.popular, name='popular'),
    url(r'^like/(?P<userID>\d*)/(?P<secretID>\d*)/(?P<page>\w*)$', views.like),
    
]
