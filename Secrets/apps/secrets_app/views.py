from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Secret
from ..login_app.models import User
from django.db.models import Count
# Create your views here.
def secrets(request):
    print "made it to secrets"
    all_secrets = Secret.objects.all().annotate(total_likes = Count('liked_by')).order_by('-created_at')
    user = User.objects.get(id = request.session['user_id'])
    

    context = {
        'all_secrets': all_secrets,
        'user_id': user.id,
        'user_name': user.first_name,
        'user': user
    }
    return render(request, 'secrets_app/secrets.html', context)
def add(request):
    addSecret_response = Secret.objects.addSecret(request.POST)
    if addSecret_response['valid']:
        return redirect('secrets:new')
    for error in addSecret_response['errors']:
        messages.error(request, error)
        print "*"*40
        print "redirecting to secrets:secrets "
        return redirect('/')
def delete(request, ID, page):
    
    Secret.objects.filter(id = ID).delete()
    if page == 'n':
        return redirect("secrets:new")
    else:
        return redirect("secrets:popular")

def popular(request):
    all_secrets = Secret.objects.all().annotate(total_likes = Count('liked_by')).order_by('-total_likes')
    user = User.objects.get(id = request.session['user_id'])
    

    context = {
        'all_secrets': all_secrets,
        'user_id': user.id,
        'user_name': user.first_name
    }

    return render(request, 'secrets_app/popular.html', context)

def like(request, userID, secretID, page):
    data = {
        'user_id':userID,
        'secret_id': secretID,
        
    }
    user = User.objects.get(id = data['user_id'])
    secret = Secret.objects.get(id = data['secret_id'])
    secret.liked_by.add(user)
    
    if page == 'p':
        return redirect("secrets:popular")
    
    return redirect('secrets:new')
    

