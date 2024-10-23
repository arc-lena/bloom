from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('complete_task/<int:task_id>/', views.toggle_task_status, name='complete_task'),
]
