from django.shortcuts import render
from django.http.response import HttpResponse


def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Bedon'}, status=200)

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'name': 'Bedon'}, status=200)

