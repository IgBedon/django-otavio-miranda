from django.shortcuts import render
from django.http.response import HttpResponse


def teste(request):
    return HttpResponse("Teste")
# Create your views here.
