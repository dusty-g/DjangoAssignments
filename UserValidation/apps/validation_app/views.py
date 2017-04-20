from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    
    return render(request, 'validation_app/index.html')
def process(request):
    # if request.method == 'POST':

    user_response = User.objects.login(request.POST)
    print 'user_response valid? ', user_response['valid']
        
        
    if not user_response['valid']:
        print "user response errors:"
        print user_response['errors']
        for error in user_response['errors']:
            messages.error(request, error)
            print " in for loop!", error
            return redirect('/')
    else:
        messages.success(request, "User " + user_response['newuser'].username+ " has been created")
        print user_response['newuser'].username
        return redirect('/success')
    return redirect('/')
def success(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "validation_app/success.html", context)