from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolioApp/index.html')

def testimonials(request):
    return render(request, 'portfolioApp/testimonials.html')