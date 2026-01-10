from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('profile/edit/<int:pk>/', views.profile_edit, name='profile_edit'),
    path('seller/create/', views.seller_create, name='seller_create'),
]
