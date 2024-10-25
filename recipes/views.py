from django.shortcuts import render
from django.http.response import HttpResponse


def teste(request):
    return render(request, 'recipes/home.html', context={'name': 'Bedon'},status=200)

