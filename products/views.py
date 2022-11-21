from django.shortcuts import render, get_object_or_404
from .models import Product

""" View to render all products page """


def all_products(request):
    
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):

    """ View to show individual product items """
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
