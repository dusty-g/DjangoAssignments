from django.shortcuts import render, redirect
import random
VALUES = ['eggs', 'bacon', 'french toast', 'pancakes','waffles', 'oatmeal', 'hashbrowns']
def index(request):
    request.session.flush()
    return render(request, 'surprise_app/index.html')

def process(request):
    if request.method == "POST":
        if request.POST['number'] == '':
            return redirect("/")
        
        count = int(request.POST["number"])
        request.session["list"] = []
        while count > 0:
            request.session["list"].append(random.choice(VALUES))
            count -= 1
        
        return redirect("/results")
    else:
        return redirect("/")

def results(request):
    if 'list' in request.session:

        context = {
            'list' : request.session['list']
        }
        return render(request, 'surprise_app/results.html', context)
    else:
        return redirect("/")
    