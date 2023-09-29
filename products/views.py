from django.http import HttpResponse
from django.template import loader
from .models import Product, ProductHistory, OnlineShop

def all_products(request):
    products = Product.objects.all().values()
    template = loader.get_template('products_page.html')
    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))

def product_detail(request, id):
    product = Product.objects.get(id=id)
    template = loader.get_template('product_detail_page.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))