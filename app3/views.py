from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def innocent(request):
    return HttpResponse('<h1> my name is aman </h1>')
    
