from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemListCreateView.as_view(), name='menu-item-list'),
    path('orders/<int:pk>/generate-receipt/', views.GenerateReceiptView.as_view(), name='generate-receipt'),
]


