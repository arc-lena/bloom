from django.contrib import admin
from .models import Task, TaskStatus

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    pass
