from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def testimonials(request):
    return render(request, 'portfolio/testimonials.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

