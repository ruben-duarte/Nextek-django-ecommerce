from django import forms

from .models import Product

class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image', )