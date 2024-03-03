from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def menu_list(request):
    categories = Category.object.all()
    product = Product.objects.all()
    

    return render(
        request, 'customer/menu.html',
        {
            'categories': categories,
            'products': products
        }
    )