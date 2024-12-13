from rest_framework import generics
from rest_framework.response import Response
from .models import MenuItem, Order, OrderItem, Inventory
from .serializers import MenuItemSerializer, OrderSerializer

class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class GenerateReceiptView(generics.GenericAPIView):
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        order_id = self.kwargs.get('pk')
        order = Order.objects.get(id=order_id)
        return self.generate_json_receipt(order)

    def generate_json_receipt(self, order):
        receipt_data = {
            'order_number': order.order_number,
            'table_number': order.table_number,
            'total_amount': order.total_amount,
            'vat_amount': order.vat_amount,
            'subtotal': order.subtotal,
            'items': [
                {
                    'menu_item': item.menu_item.name,
                    'quantity': item.quantity,
                    'price': item.price,
                    'total': item.total_price,
                } for item in order.items.all()
            ]
        }
        return Response(receipt_data)










