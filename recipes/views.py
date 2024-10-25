from django.shortcuts import render
from django.http.response import HttpResponse


def teste(request):
    return render(request, 'home.html')
# Create your views here.
