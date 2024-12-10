# restaurant/models.py

from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('drink', 'Drink'),
        ('dessert', 'Dessert'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    table_number = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    payment_status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order {self.order_number}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

class Inventory(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)
    low_stock_alert = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name
