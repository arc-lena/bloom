from django.contrib import admin
from .models import Task, TaskStatus

from django.contrib import admin
from .models import Task, TaskStatus

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Поля, які будуть відображені у списку завдань
    list_display = ('title', 'description')
    search_fields = ('title',)  # Пошук по полю назви
    ordering = ('title',)  # Сортування за назвою

@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    # Поля, які будуть відображені у списку статусів завдань
    list_display = ('task', 'user', 'completed')
    list_filter = ('completed', 'user')  # Фільтри для статусу виконання та користувача
    search_fields = ('task__title', 'user__username')  # Пошук за назвою завдання та ім'ям користувача
    ordering = ('user', 'task')  # Сортування за користувачем і завданням

