from django.urls import path
from . import views

urlpatterns = [
    # MenuItem endpoints
    path('menu-items/', views.MenuItemListCreateView.as_view(), name='menu-item-list'),
    path('menu-items/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-item-detail'),

    # Order endpoints
    path('orders/', views.OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),

    # OrderItem endpoints
    path('order-items/', views.OrderItemListCreateView.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', views.OrderItemDetailView.as_view(), name='order-item-detail'),

    # Inventory endpoints
    path('inventory/', views.InventoryListCreateView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', views.InventoryDetailView.as_view(), name='inventory-detail'),
]

