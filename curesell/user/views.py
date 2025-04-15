from django.shortcuts import render,redirect, HttpResponse
from .models import *
from django.conf import settings

# def welcome(request):
#     return HttpResponse("Testing: Hello World!")

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'login.html')
    
def register(request):
    return render(request,'register.html')
    
def verification(request):
    return render(request,'verification.html')
    