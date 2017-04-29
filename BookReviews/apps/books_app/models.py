from __future__ import unicode_literals
from ..users_app.models import User
from django.db import models



class Author(models.Model):
    name = models.TextField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookManager(models.Manager):
    def addBook(self, postData):
        
        if not postData:
            return False
        if len(postData['review']) < 2:
            return False
        if postData['author']:
            author = Author.objects.create(name = postData['author'])
        else:
            print postData['author-select']
            author = Author.objects.get(name = postData['author-select'])
        newBook = Book.objects.create(title = postData['title'], author = author)
        user = User.objects.get(id = postData['user'])
        newReview = Review.objects.create(review = postData['review'], stars = postData['stars'], user = user, book = newBook)
        return newBook.id

    def addReview(self, postData):
        if not postData:
            return False
        if len(postData['review']) < 2:
            return False
        book = Book.objects.get(id = postData['book_id'])
        user = User.objects.get(id = postData['user_id'])
        
        newReview = Review.objects.create(review = postData['review'], stars = postData['stars'], user = user, book = book)
        return newReview
    
class Book(models.Model):
    title = models.TextField(max_length=100)
    author = models.ForeignKey(Author, null = True, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    review = models.TextField(null = True)
    stars = models.IntegerField(null = True)
    user = models.ForeignKey(User, null = False, related_name='reviews')
    book = models.ForeignKey(Book, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
