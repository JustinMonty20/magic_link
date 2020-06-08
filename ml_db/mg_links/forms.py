from django import forms

class AddProduct(forms.Form):
    product_name = forms.CharField(max_length=200)
    key_word = forms.CharField(max_length=200)
    link = forms.CharField(max_length=500) 