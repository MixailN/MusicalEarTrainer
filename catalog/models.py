from django.db import models

CHOICES = (
    ('A', 'Guess the Note'),
    ('B', 'Guess the chord key'),
)


# Create your models here.
class Task(models.Model):
    answer = models.CharField(max_length=100)
    task_sound = models.FileField(upload_to='sounds')

    def __str__(self):
        return 'Task ' + self.answer


class Exercise(models.Model):
    exercise_type = models.CharField(max_length=150, choices=CHOICES)
    exercise_title = models.CharField(max_length=150)
    exercise_description = models.TextField()
    tasks = models.ManyToManyField(Task, blank=True)

    def __str__(self):
        return self.exercise_title
