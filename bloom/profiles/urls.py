from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.profile_settings_view, name='profile_set'),
]

