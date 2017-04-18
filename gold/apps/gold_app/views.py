from django.shortcuts import render, redirect
from random import randint
# Create your views here.



def index(request):
    
    if ("gold" in request.session):
        print "there's a session already"
        context = {
            'gold': request.session["gold"],
            "activities": request.session['activities']
        }
        return render(request, "gold_app/index.html", context)
    else:
        
        request.session["gold"] = 0
        request.session["activities"] = []
        context = {
            'gold': request.session["gold"],
            "activities": request.session['activities']
        }
        return render(request, "gold_app/index.html", context)


    

def process(request):
    def getGold(a, b):
    
        activityString = "Earned "
        amount = randint(a, b)
        request.session["gold"] = request.session["gold"] + amount
        activityString += str(amount)
        activityString += " from the " + request.POST["building"]
        request.session["activities"].append(activityString)
        

        return redirect("/")
    if request.method == "POST":
        if request.POST["building"] == "cave":
            return getGold(5,10)
    if request.method == "POST":
        if request.POST["building"] == "farm":
            return getGold(5,10)
    if request.method == "POST":
        if request.POST["building"] == "house":
            return getGold(5,10)
    if request.method == "POST":
        if request.POST["building"] == "casino":
            return getGold(5,10)
    else:
        return redirect("/")
def reset(request):
    request.session.flush()
    return redirect("/")



