from django.shortcuts import render
from django.http import Http404
from .models import Exercise
from .forms import AnswerForm
# Create your views here.
EXERCISE_TYPES = []


def catalog(request):
    exercises = Exercise.objects
    return render(request, 'catalog/catalog.html', {'exercises': exercises})


def get_exercise(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    exercise = Exercise.objects.get(id=offset)
    print(exercise.exercise_title)
    return render(request, 'catalog/exercise.html', {'exercise': exercise})

