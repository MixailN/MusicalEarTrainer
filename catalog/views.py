from django.shortcuts import render
from django.http import Http404
from .models import Exercise
from .models import Task
from .possible_answers import create_form
from django.http import JsonResponse

# Create your views here.
EXERCISE_TYPES = []


def catalog(request):
    exercises = Exercise.objects
    return render(request, 'catalog/catalog.html', {'exercises': exercises})


def get_exercise(request, offset):
    try:
        offset = int(offset)
        exercise = Exercise.objects.get(id=offset)
        tasks = list(exercise.tasks.all())
        tasks = [tmp.id for tmp in tasks]
    except ValueError:
        raise Http404()
    except Exercise.DoesNotExist:
        raise Http404()
    return render(request, 'catalog/exercise.html', {'exercise': exercise, 'tasks': tasks})


def get_task(request):
    if request.method == 'GET':
        try:
            task = Task.objects.get(id=int(request.GET['q']))
        except ValueError:
            raise Http404()
        except Exercise.DoesNotExist:
            raise Http404()
        except Exception:
            raise Http404()
        form = create_form(task.task_type, task.answer)
        return render(request, 'catalog/task.html', {'task': task, 'form': form})
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=int(request.GET['q']))
            answer = request.GET['ans']
        except Exception:
            raise Http404()
        response_data = {
            'is_right': task.answer == answer,
            'answer': task.answer
        }
        return JsonResponse(response_data)
