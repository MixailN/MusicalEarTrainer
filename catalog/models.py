from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Exercise(models.Model):
    exercise_title = models.CharField(max_length=150)
    exercise_description = models.TextField()
    exercise_sound = ArrayField(models.FileField(upload_to='sounds'))
