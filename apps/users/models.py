from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    USER_STATUS_CHOICES = (
        ('USER', 'User'),
        ('SELLER', 'Seller'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=USER_STATUS_CHOICES, default='USER')

    def __str__(self):
        return f"{self.user.username} - {self.status}"


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    shop_name = models.CharField(max_length=255)

    def __str__(self):
        return self.shop_name
