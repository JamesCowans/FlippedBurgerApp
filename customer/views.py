from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def menu_list(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    

    return render(
        request, 'product/menu.html',
        {
            'categories': categories,
            'product': product
        }
    )