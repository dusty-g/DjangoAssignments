from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
def index(request):
    return render(request, 'users_app/index.html')
def displayUser(request, userID):
    return render(request, 'users_app/users.html')

def register(request):
    register_response = User.objects.register(request.POST)
    if register_response['valid']:
        
        print 'about to redirect to books:books'
        request.session['username'] = register_response['user'].alias
        request.session['user_id'] = register_response['user'].id
        return redirect('books:books')

    else:
        for error in register_response['errors']:
            messages.error(request, error)
        print "about to redirect to /"
        return redirect('/')
    

def login(request):
    login_response = User.objects.login(request.POST)
    if login_response['valid']:
        request.session['username'] = login_response['user'].alias
        request.session['user_id'] = login_response['user'].id
        return redirect('books:books')
    else:
        for error in login_response['errors']:
            messages.error(request, error)
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('users:login')