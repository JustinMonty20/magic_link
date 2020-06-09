from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import AddProduct
from .models import Product


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            name = form.cleaned_data['product_name']
            key = form.cleaned_data['key_word']
            url = form.cleaned_data['link']
            new_item = Product.objects.create(product_name=name,key_word=key,link=url)
            new_item.save()
            return HttpResponseRedirect('/added/')
    else:
        form = AddProduct()
    return render(request,'mg_links/add_product.htm', {'form':AddProduct})


class SearchView(TemplateView):
    template_name = 'search.htm'

class AddedView(TemplateView):
    template_name = 'added.htm'


        

    
    
    

    