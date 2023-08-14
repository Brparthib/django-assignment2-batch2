from django import forms
from first_app.models import TaskModel
from django.forms import Textarea, BooleanField


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_title', 'task_description']
        widgets = {
            'task_description': Textarea(attrs={'cols': 30, 'rows': 5})
        }
        labels = {
            'task_title': 'Title: ',
            'task_description': 'Description: '
        }
        

class TaskCompleteModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['is_completed']
        labels = {
            'is_completed': 'Check Completed: ',
        }
        