from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.partner_list, name='partner_list'),
    path('partners/', include('partners.urls')),
    path('use-points/<int:partner_id>/', views.use_points, name='use_points'),
]
