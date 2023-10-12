from django.shortcuts import render
from product_store.models import Product

def homepage(request):
    products = Product.objects.all().filter(product_availability=True)
    # above line fetch all objects of that model to the variable
    context = {
        'products':products 
    }
    return render(request, 'homepage.html', context)