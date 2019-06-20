from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from about.models import *
from datetime import *
# Create your views here.

@csrf_exempt
def splash(request):
    if request.method == "POST":
        date = datetime.now()
        name = str(request.POST["username"])
        if TwitterUser.allUsers.__contains__(name):
            obj = TwitterUser.allUsers.get(name)
            new_tweet = obj.generate_tweet()
            return render(request, "tweet.html", context = {'string':new_tweet, 'date':date, 'name':name})
        else:
            #account for the case where the requested user has a private profile or does not extist
            try:
                obj = TwitterUser(name)
                new_tweet = obj.generate_tweet()
                return render(request, "tweet.html", context = {'string':new_tweet, 'date':date, 'name':name})
            except:
                return redirect('/exception')
    else:
        return render(request, "welcome.html", {})

def exception(request):
    return render(request, "exception.html", {})