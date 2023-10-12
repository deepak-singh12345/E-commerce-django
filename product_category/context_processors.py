from . models import Product_category

def menu_links(request):
    links = Product_category.objects.all()
    return dict(links=links)