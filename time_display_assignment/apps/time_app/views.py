from django.shortcuts import render
from datetime import datetime




# Create your views here.
def index(request):

    test = datetime.now().strftime('%b %d, %Y')
    time = datetime.now().strftime('%I:%M %p')
    

    data = {
        'date': test,
        'time': time
    }
    print test
    return render(request, 'index.html', data)