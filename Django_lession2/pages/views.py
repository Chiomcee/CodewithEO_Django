from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
# function-based vs class-based
# takes in an Http request and returns an http response

# homepage
def home(request):
    # return HttpResponse("<h1>Home  Page")
    return render(request, 'pages/home.html')

# about us
def about(request):
    # return HttpResponse("<h1>About us  Page")
    return render(request, 'pages/about.html')

# contact us
def contact(request):
    # return HttpResponse("<h1>Contact us  Page")
    return render(request, 'pages/contact.html')

# services
def services(request):
    # return HttpResponse("<h1>Services  Page")
    return render(request, 'pages/services.html')

