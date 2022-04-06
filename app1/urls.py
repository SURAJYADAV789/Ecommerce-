from unicodedata import name
from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('home',home,name='home'),
    path("customer_products",customer_products,name='customer_products'),

    path('products',ProductView.as_view(), name='products'),
    path("addproduct",ProductCreateView.as_view(),name='addproduct'),
    path('product-update/<pk>',ProductUpdateView.as_view(),name='product-update'),
    path('product-delete/<pk>',ProductDeleteView.as_view(),name='product-delete'),
    path('product-detail/<pk>',ProductDetailView.as_view(),name='product-detail'),
    
    path("components",components),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

