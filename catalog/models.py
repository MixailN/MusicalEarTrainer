from django.db import models

CHOICES = (
    (0, 'Guess the Note'),
    (1, 'Guess the Chord Key'),
    (2, 'Guess the Interval')
)


# Create your models here.
class Task(models.Model):
    answer = models.CharField(max_length=100)
    task_type = models.IntegerField(choices=CHOICES)
    task_sound = models.FileField(upload_to='sounds')

    def __str__(self):
        return 'Task ' + self.answer


class Exercise(models.Model):
    exercise_title = models.CharField(max_length=150)
    exercise_description = models.TextField()
    tasks = models.ManyToManyField(Task, blank=True)

    def __str__(self):
        return self.exercise_title
