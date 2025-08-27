from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1 style='color:blue;'>Hello, world!</h1>")


def hello(request):
    return HttpResponse("<h1 style='color:pink;'>Welcome to the home page!</h1>")

def home(request):
    return render(request,"index.html")
