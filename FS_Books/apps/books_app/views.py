from django.shortcuts import render, redirect
from .models import Books

def index(request):
    
    context = {
        'books': Books.objects.all()
    }
    return render(request, 'books_app/index.html', context)

def add(request):
    if request.method == "POST":
        book = Books(title = request.POST['title'], author = request.POST['author'], category = request.POST['category'])
        book.save()
        
    return redirect('/')
