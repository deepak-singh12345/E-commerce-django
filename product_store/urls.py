from django.urls import path
from .import views

urlpatterns = [
    path('', views.product_store, name='product_store'),
    path('category/<slug:category_slug>/', views.product_store, name='products_by_category'),
    # in above url slug is not a variable bu a converter example : str, int, uuid
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='single_product_detail'),
    path('search/', views.search, name='search'),
]