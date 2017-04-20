from django.shortcuts import render, redirect
from .models import Courses
# Create your views here.
def index(request):
    context = {
        'courses': Courses.objects.all(),
    }
    return render(request, 'courses_app/index.html', context)

def destroy(request, urlID):
    course = Courses.objects.get(id = urlID)
    context = {
        'course': course
    }
    return render(request, 'courses_app/destroy.html', context)

def add(request):
    if request.method == "POST":
        course = Courses(name = request.POST['name'], description = request.POST['description'])
        course.save()
        
    return redirect("/")
def delete(request, urlID):
    Courses.objects.filter(id = urlID).delete()
    return redirect("/")