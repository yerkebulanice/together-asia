from tabnanny import verbose
from django.db import models

class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'