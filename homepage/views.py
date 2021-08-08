from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def HomeView(request):
    return render(request, "homepage/home.html")

def AboutView(request):
    return render(request, "homepage/about.html")

def BlogView(request):
    return render(request, "homepage/blog.html")