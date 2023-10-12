from django.db import models
from django.urls import reverse 

# Create your models here.

class Product_category(models.Model):
    category_name = models.CharField(max_length=50, unique = True)
    product_slug = models.SlugField(max_length=50, unique=True)
    product_description = models.TextField(max_length=512, blank=True)
    category_image = models.ImageField(upload_to = 'photos/categories', blank=True)

    class Meta:
        verbose_name = 'Product_category'
        verbose_name_plural = 'Product_categories'

    def get_category_url(self):
        return reverse('products_by_category', args=[self.product_slug])

    def __str__(self):

        return self.category_name