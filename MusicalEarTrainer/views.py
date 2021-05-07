from django.shortcuts import render
from catalog.models import Exercise


def home(request):
    exercises = Exercise.objects
    return render(request, 'home.html', {'exercises': exercises})
