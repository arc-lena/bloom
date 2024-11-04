from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import Task, TaskStatus
from django.contrib.auth.models import User

@login_required
def homepage(request):
    statuses = TaskStatus.objects.filter(user=request.user, selected=True)
    return render(request, 'tasks/index.html', {'statuses': statuses})

@login_required
def toggle_task_status(request, task_id):
    if request.method == 'POST':
        task_status = get_object_or_404(TaskStatus, task_id=task_id, user=request.user)
        task_status.toggle_completion()
        return JsonResponse({'completed': task_status.completed})