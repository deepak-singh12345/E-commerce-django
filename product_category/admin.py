from django.contrib import admin
from . models import Product_category

# Register your models here.
class Product_category_admin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug':('category_name',)}
    list_display = ('category_name', 'product_slug')

admin.site.register(Product_category, Product_category_admin)