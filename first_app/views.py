from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from first_app.forms import TaskModelForm
from first_app.models import TaskModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from first_app.forms import TaskCompleteModelForm


# Create your views here.
class AddTaskView(CreateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('show_tasks')
    

class TaskListView(ListView):
    model = TaskModel
    template_name = 'show_tasks.html'
    context_object_name = 'data'
    
class DeleteTaskView(DeleteView):
    model = TaskModel
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('show_tasks')
    
class EditTaskView(UpdateView):
    model = TaskModel
    form_class = TaskModelForm
    template_name = 'edit_task.html'
    success_url = reverse_lazy('show_tasks')
    
class CompletedTaskView(UpdateView):
    model = TaskModel
    form_class = TaskCompleteModelForm
    template_name = 'fill_complete_task.html'
    success_url = reverse_lazy('completed_tasks')
    
class CompletedTaskListView(ListView):
    model = TaskModel
    template_name = 'completed_tasks.html'
    context_object_name = 'data'
