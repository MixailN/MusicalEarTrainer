from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Task(models.Model):
    answer = models.CharField(max_length=100)
    task_sound = models.FileField(upload_to='sounds')


class Exercise(models.Model):
    exercise_title = models.CharField(max_length=150)
    exercise_description = models.TextField()
    tasks = models.ManyToManyField(Task, blank=True)
