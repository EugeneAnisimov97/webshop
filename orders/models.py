from django.db import models
from users.models import User
from tovars.models import Tovars

# Create your models here.
class Orders(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Ожидание'),
        ('processing', 'В обработке'),
        ('completed', 'Завершён'),
        ('canceled', 'Отменён'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Order #{self.id} by {self.user.username} - Status: {self.get_status_display()}'

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, related_name='items', on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovars, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.tovar.name}'