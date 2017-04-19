from django.shortcuts import render, redirect

def index(request):
    return render(request, 'landscapes_app/index.html')

def process(request, id):
    print id
    print range(1,10)
    if int(id) in range(0, 11):
        image = "snow.jpeg"
    elif int(id) in range(11, 21):
        image = "desert.jpeg"
    elif int(id) in range(21, 31):
        image = 'forest.jpeg'
    elif int(id) in range(31,41):
        image = 'vineyard.jpeg'
    else:
        image = "tropical.jpeg"
    context = {
        "image": image
    }
    return render(request, "landscapes_app/landscapes.html", context)

