# app1/views.py
from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'app1/home.html')

def about(request):
    return render(request, 'app1/about.html')

def contact(request):
    return render(request, 'app1/contact.html')
