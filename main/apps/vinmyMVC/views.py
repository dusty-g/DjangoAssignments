from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'vinmyMVC/index.html')

def show(request):
    print(request.method)
    return render(request,'vinmyMVC/show_users.html')
def create(request):
    if request.method == "POST":
        print "*"*30
        print request.POST
        print request.method
        print "*"*30
        return redirect("/show")
    else:
        return redirect("/")