from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=50,unique=True)
    content = models.TextField(verbose_name=_("Content"), max_length=100)
    time_created = models.DateTimeField(verbose_name=_("Time created"), auto_now_add=True)
    time_update = models.DateTimeField(verbose_name=_("Time created"), auto_now=True)
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name