from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    #if not request.user.is_authenticated:
    #    return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/user.html")
    #return HttpResponseRedirect(request.GET.get('next'))

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        valuenext = request.POST["next"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if valuenext:
                return HttpResponseRedirect(valuenext)
            else:
                return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {
                "message":"Invalid credentials."
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    #return render(request, "users/login.html", {"message":"Logged ouot"})
    return HttpResponseRedirect(reverse("users:index"))