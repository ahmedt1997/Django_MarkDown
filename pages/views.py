from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template.context_processors import request


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')
