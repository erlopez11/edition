from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Edition Home Page</h1>')
