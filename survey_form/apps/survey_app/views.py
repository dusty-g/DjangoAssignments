from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey_app/index.html')

# view to take in form data
def process(request):
    print "form works..."
    if request.method == "POST":
        print "*"*50
        print "post method"
        print request.POST
        if "count" in request.session:
            request.session["count"] += 1
        else:
            request.session["count"] = 1
        request.session["name"] = request.POST["name"]
        request.session["location"] = request.POST["location"]
        request.session["language"] = request.POST["language"]
        request.session["comment"] = request.POST["comment"]
        return redirect("/results")
    else:
        print "*"*50 
        print "not post"
    return redirect("/")
#view to render results page
def results(request):
    
    return render(request, 'survey_app/results.html')