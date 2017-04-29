from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Book, Review, Author

def books(request):
    print 'made it to the books app'
    print request.session['username']
    recent_reviews = Review.objects.all().order_by('-created_at')
    all_books = Book.objects.all()
    context = {
        'reviews': recent_reviews,
        'user_id': request.session['user_id'],
        'books': all_books

    }
    return render(request, 'books_app/books.html', context)

def book(request, bookID):
    print 'bookID....'
    print bookID
    book = Book.objects.get(id = bookID)
    reviews = Review.objects.filter(book = book)
    context = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'books_app/book.html', context)

def addPage(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books_app/add.html', context)
def addBook(request):
    newBookID = Book.objects.addBook(request.POST)
    print newBookID

    return redirect('/books/'+str(newBookID))

def delete(request, reviewID):
    print reviewID
    return redirect('books:books')

def review(request, bookID):
    Book.objects.addReview(request.POST)

    urlstr = '/books/'+bookID
    return redirect(urlstr)