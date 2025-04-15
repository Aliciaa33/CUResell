from django.shortcuts import render,redirect, HttpResponse
from .models import *
from django.conf import settings

def product_info(request):
    return render(request,'product_info.html')

def ProductPost(request):
    return render(request,'ProductPost.html')

def search_default(request):
    return render(request,'search_default.html')