from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemListCreateView.as_view(), name='menu-item-list'),
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),  # To list and create orders
    path('orders/<int:pk>/', views.OrderRetrieveView.as_view(), name='order-retrieve'),  # Retrieve a specific order
    path('orders/<int:pk>/generate-receipt/', views.GenerateReceiptView.as_view(), name='generate-receipt'),
]



