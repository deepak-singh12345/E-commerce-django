from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q 
from carts.models import CartItem
from carts.views import _get_cart_id

from product_store.models import Product
from product_category.models import Product_category

# Create your views here.

def product_store(request, category_slug=None):
    categories=None
    products = None
    products_count=None 

    if category_slug != None:
        categories = get_object_or_404(Product_category, product_slug=category_slug)
        products= Product.objects.filter(category_name=categories, product_availability=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(product_availability=True).order_by('id')
        # products_count = products.count()
        # above line fetch all objects of that model to the variable
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    context = {
        'products':paged_products,
        'products_count':products_count 
    }
    return render(request, 'product_store/product_store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product_detail = Product.objects.get(category_name__product_slug=category_slug, product_slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_get_cart_id(request), product=single_product_detail).exists()
    except Exception as e:
        raise e
    context = {
        'single_product_detail':single_product_detail,
        'in_cart':in_cart,
    }
    return render(request, 'product_store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_at').filter(Q(product_description__icontains=keyword) | Q(product_name__icontains = keyword))
        context= {
            'products':products,
        }
    return render(request, 'product_store/product_store.html', context)