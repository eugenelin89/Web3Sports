# *** NOT BEING USED ***
# Original Setup file

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request, "mybusiness/index.html")

'''
NBF - New Business Form

'''
@login_required
def new_business(request):
    return render(request, "mybusiness/new_business.html")
