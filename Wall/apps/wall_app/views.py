from django.shortcuts import render, redirect
from .models import Users, Messages, Comments
# Create your views here.
def load(request):
    user1 = Users.objects.create(first_name = 'Jack', last_name = 'Reacher', email='n3vrG0b@ack.com', password='rosebud')

    user12 = Users.objects.get(id = 12)
    message1 = Messages.objects.create(user = user1 , message = 'my name is jack')
    
    
    Comments.objects.create(message = message1, user = user12, comment="hello jack!, I'm bob")
    
    return redirect('/')
def index(request):
    users = Users.objects.all()
    messages = Messages.objects.all()
    comments = Comments.objects.all()

    context = {
        'users': users,
        'messages': messages,
        'comments': comments
    }
    return render(request, 'wall_app/index.html', context)