from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddTaskView.as_view(), name='add_task'),
    path('show_tasks/', views.TaskListView.as_view(), name='show_tasks'),
    path('completed_tasks/', views.CompletedTaskListView.as_view(), name='completed_tasks'),

    # Delete, Edit & Completed Path
    path('delete_task/<int:pk>', views.DeleteTaskView.as_view(), name='delete_task'),
    path('edit_task/<int:pk>', views.EditTaskView.as_view(), name='edit_task'),
    path('fill_complete_task/<int:pk>',
         views.CompletedTaskView.as_view(), name='fill_complete_task'),
]
