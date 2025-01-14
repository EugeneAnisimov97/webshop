from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)  # Добавляем поле для телефона
    address = models.CharField(max_length=255, blank=True, null=True)  # Добавляем поле для адреса
    
    
    def __str__(self):
        return self.get_full_name()