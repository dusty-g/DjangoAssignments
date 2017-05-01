from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Note
from .forms import noteForm
# Create your views here.
def index(request):
    
    form = noteForm()
    all_notes = Note.objects.all()
    
    context = {
        'notes': all_notes,
        'form': form
    }
    
    return render(request, 'posts_app/index.html', context)
def process(request):
    if not Note.objects.addNote(request.POST):   
        messages.error(request, 'Cannot post empty note')

    return render(request, 'posts_app/posts_index.html', {'notes': Note.objects.all()})