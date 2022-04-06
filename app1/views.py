from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from app1.forms import ProductForm
from .models import *


def home(req):
    return render(req,'app1/home.html')

def customer_products(req):
    products=Product.objects.all()
    context={'products':products}
    return render(req,'customer/products.html',context)

class ProductCreateView(CreateView):
    model = Product
    form_class=ProductForm
    template_name = 'app1/products.html'
    success_url = reverse_lazy('products')
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        data = super().get_context_data()
        
        data['product_list'] = Product.objects.all()
        data.setdefault('action','add')
        return data


class ProductView(ListView):
    template_name = 'app1/products.html'
    model = Product
    context_object_name='product_list'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "app1/products.html"
    form_class=ProductForm
    success_url=reverse_lazy('products')

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['action']='update'
        data['product_list']=Product.objects.all()
        return  data

class ProductDeleteView(DeleteView):
    model=Product
    success_url=reverse_lazy('products')

class ProductDetailView(DetailView):
    model=Product
    template_name='app1/products.html'

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        print("data",data,type(data))
        # data['product']=Product.objects.get()
        data['action']='detail'
        return  data


def signin(req):
    return render(req,'app1/signin.html')

def signup(req):
    return render(req,'app1/signup.html')

def components(req):
    return render(req,'app1/components.html')