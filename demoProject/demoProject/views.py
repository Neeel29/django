from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
  # return HttpResponse("Hello, World! Home page")
  return render(request, 'website/index.html')

def About(request):
  return HttpResponse("Hello, World! About Page")

def Contact(request):
  return HttpResponse("Hello, World! Contact Page")