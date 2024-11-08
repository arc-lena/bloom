from django.urls import path
from . import views

urlpatterns = [
    path('', views.partner_list, name='partner_list'),
    path('redeem/<int:partner_status_id>/', views.redeem, name='redeem'),
]
