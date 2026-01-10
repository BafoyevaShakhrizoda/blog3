from django import forms
from .models import User, Profile, Seller
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'status']


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['user', 'shop_name']
