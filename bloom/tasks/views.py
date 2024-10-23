from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Task, TaskStatus

@login_required
def homepage(request):
    tasks = Task.get_random_tasks(request.user)
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def toggle_task_status(request, task_id):
    if request.method == 'POST':
        task_status = get_object_or_404(TaskStatus, task_id=task_id, user=request.user)
        task_status.toggle_completion()
        return JsonResponse({'completed': task_status.completed})
