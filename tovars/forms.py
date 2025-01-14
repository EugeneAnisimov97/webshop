from django import forms
from .models import Tovars

class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovars
        fields = ['name', 'description', 'price','stock', 'image', 'category'] 