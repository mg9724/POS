from rest_framework import generics
from .models import MenuItem, Order, OrderItem, Inventory
from .serializers import MenuItemSerializer, OrderSerializer, OrderItemSerializer, InventorySerializer

# View to handle MenuItems
class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# View to handle single MenuItem (retrieve, update, delete)
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# View to handle Orders (List and Create Orders)
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# View to handle single Order (Retrieve, Update, Delete)
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# View to handle OrderItems (List and Create Order Items)
class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# View to handle single OrderItem (Retrieve, Update, Delete)
class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# View to handle Inventory (List and Create Inventory Items)
class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

# View to handle single Inventory Item (Retrieve, Update, Delete)
class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer




