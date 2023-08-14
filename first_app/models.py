from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=30)
    task_description = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)