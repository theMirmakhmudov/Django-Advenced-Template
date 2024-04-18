from django import forms
from .models import Product


class HotelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image']
