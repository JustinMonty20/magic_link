from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,View
from django.template import RequestContext
from .forms import AddProduct, SearchProduct
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

class SearchView(View):
    def get(self,request):
        template_name = 'search.htm'
        form = SearchProduct(request.GET or None)
        if form.is_valid():
            results = Product.objects.filter(key_word=form.cleaned_data['looking_for'])
        else: 
            results = None
        return render(request, template_name, {'form':form,'results':results})
class AddedView(TemplateView):
    template_name = 'added.htm'







        

    
    
    

    