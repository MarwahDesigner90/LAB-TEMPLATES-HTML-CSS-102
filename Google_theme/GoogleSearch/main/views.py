from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.

def home_view(request :HttpRequest):
    return render(request , "main/home.html")

def base_view(request :HttpRequest):
    return render(request ,"main/base.html")

def terms_view(request :HttpRequest):
    return render(request ,"main/terms.html")