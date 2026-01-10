from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:id>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:id>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
]

