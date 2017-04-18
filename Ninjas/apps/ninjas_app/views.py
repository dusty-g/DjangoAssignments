from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninjas_app/index.html')

def ninjas(request, color):
    colors = ["blue", "red", "orange", "purple"]
    if color == "":
        color = "tmnt"
        file = ".png"
    elif color in colors:
        file = ".jpg"
    else:
        color = "april"
        file = ".jpg"
    

    context = {
        'img': color,
        'file': file
    }
    return render(request, 'ninjas_app/ninjas.html', context)