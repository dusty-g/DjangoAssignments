from django.shortcuts import render, redirect
import random, string

def index(request):
    if "word" in request.session:
        print "word in session...."
    else:
        request.session["word"] = "Click to Generate Word"
        request.session["count"] = 0
    
    return render(request, 'word_app/index.html')

def generate(request):
    word = ''.join(random.choice(string.lowercase) for i in range(14))
    print "*"*40
    print word
    request.session["word"] = word
    request.session["count"] += 1
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect("/")