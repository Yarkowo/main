from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def home(response):
    return HttpResponse("hola home")

def carreras(response):
    return HttpResponse("hola carreras")

def docentes(response):
    return HttpResponse("hola docentes")