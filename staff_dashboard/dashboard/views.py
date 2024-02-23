from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Staff

def home(request):
    file = loader.get_template('home.html')
    return HttpResponse(file.render())
