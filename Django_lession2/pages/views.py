from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
# function-based vs class-based
# takes in an Http request and returns an http response

# homepage
def home(request):
    return HttpResponse("<h1>Home  page")

# about us
def about(request):
    return HttpResponse("<h1>About us  page")

# contact us
def contact(request):
    return HttpResponse("<h1>Contact us  page")

# services
def services(request):
    return HttpResponse("<h1>Services  page")

