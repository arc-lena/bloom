from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from .views import profile_view


urlpatterns = [
    path('', views.home, name='home'),  # Головна сторінка
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
]
