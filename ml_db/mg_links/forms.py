from django import forms
from .models import Product

class AddProduct(forms.Form):
    product_name = forms.CharField(max_length=200, label='Product name ')
    key_word = forms.CharField(max_length=200, label='Key_word ')
    link = forms.CharField(max_length=500, label='Add link here ') 

    class Meta:
        model = Product 


class SearchProduct(forms.Form):
    looking_for = forms.CharField(max_length=200, label='Search by key_word ')

