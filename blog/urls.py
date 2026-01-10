from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('', views.profile, name='profile'),
]
