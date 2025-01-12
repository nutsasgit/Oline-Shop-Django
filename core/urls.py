from django.urls import path
from .views import productlistView, createProductView, productDetailView, productUpdateView, productDeleteView

urlpatterns = [
    path('product-list', productlistView, name='product-list'),
    path('create-product', createProductView, name='create-product'),
    path('product-detail/<slug:product_id>/', productDetailView, name='product-detail'),
    path('product-update/<slug:product_id>/', productUpdateView, name='product-update'),
    path('product-delete/<slug:product_id>/', productDeleteView, name='product-delete')
]