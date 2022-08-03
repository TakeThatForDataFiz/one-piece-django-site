from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# create temp sample view to be replaced


def index(request):
    return HttpResponse("Hello World, you are at the news index")
