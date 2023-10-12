from django.contrib import admin
from .models import Product, Variation
# Register your models here.

class Product_admin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'product_stock', 'category_name', 'modified_at', 'product_availability']
    prepopulated_fields = {'product_slug':('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display=['product', 'variation_category', 'variation_value', 'is_active']
    list_editable = ['is_active',]
    list_filter = ['product', 'variation_category', 'variation_value']

admin.site.register(Product, Product_admin)
admin.site.register(Variation, VariationAdmin)