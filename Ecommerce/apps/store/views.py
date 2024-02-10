from django.shortcuts import render ,get_object_or_404

# Create your views here.
from .models import Product

def  product_detail(request , slug):
    print('slug:',slug)
    product=get_object_or_404(Product,slug=slug)

    return render (request , 'product_detail.html', {'product':product})