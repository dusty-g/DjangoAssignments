from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')
    
def login(request):
    user = User.objects.login(request.POST)
    if user['valid']:
       
        
        request.session['user_id'] = user['user_id']

        return redirect("/success")
    else:
        for error in user['errors']:
            messages.error(request, error)
        return redirect('/')
def process(request):
    user = User.objects.register(request.POST)
    
    
    if user['valid']:
        print "user was vaild!"
        print user['user_id']
        request.session['user_id'] = user['user_id']
        return redirect('/success')
    for i in user['errors']:
        messages.error(request, i)
    return redirect("/")

def success(request):
    return redirect('secrets:new')