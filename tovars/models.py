from django.db import models
from shop.models import Shop

# Create your models here.
class Tovars(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='tovars/', blank=True, null=True)
    category = models.ForeignKey(Shop, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name