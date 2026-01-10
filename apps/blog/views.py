from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Product,Category


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'


class ProductCreateView(CreateView):
    model = Product
    fields = ['category', 'title', 'description', 'price', 'stock', 'is_available']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')



class ProductUpdateView(UpdateView):
    model = Product
    fields = ['category', 'title', 'description', 'price', 'stock', 'is_available']
    template_name = 'product_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('product_list')

class CategoryCreateView(CreateView):
    model = Category
    fields = ['title']
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'