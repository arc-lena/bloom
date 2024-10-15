from django.urls import path
from . import views

urlpatterns = [
    path('', views.partner_list, name='partner_list'),
    path('use-points/<int:partner_id>/', views.use_points, name='use_points'),
]
