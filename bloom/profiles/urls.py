from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'), 
    path('profile/', views.profile_view, name='profile'),
    path('statistics/', views.leaderboard_and_statistics_view, name='statistics'),  
    path('settings/', views.profile_settings_view, name='profile_set'),
    path('delete_user/', views.delete_account, name='delete_user'), 
]
