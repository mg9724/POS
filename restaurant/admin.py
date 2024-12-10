from django.contrib import admin
from django.contrib import admin
from .models import MenuItem, Order, OrderItem, Inventory

admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Inventory)


