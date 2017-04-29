from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^(?P<bookID>\d+)$', views.book),
    url(r'^$', views.books, name='books'),
    url(r'^add$', views.addPage, name='add'),
    url(r'^addbook', views.addBook, name='addBook'),
    url(r'^delete/(?P<reviewID>\d+)', views.delete),
    url(r'^review/(?P<bookID>\d+)', views.review),
    
]
