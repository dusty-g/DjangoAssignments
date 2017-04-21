from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')
    
def login(request):
    user = User.objects.login(request.POST)
    if user['valid']:
        request.session['first_name'] = user['user'].first_name
        return redirect("/success")
    else:
        for i in user['errors']:
            messages.error(request, i)
        return redirect('/')
def process(request):
    user = User.objects.register(request.POST)
    print user
    if user['valid']:
        print "user was vaild!"
        request.session['first_name'] = user['user'].first_name 
        return redirect('/success')
    for i in user['errors']:
        messages.error(request, i)
    return redirect("/")

def success(request):
    return render(request, "login_app/success.html")