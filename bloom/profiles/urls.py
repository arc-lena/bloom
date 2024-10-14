from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Головна сторінка
    path('', views.partners_view, name='partners'),
]
