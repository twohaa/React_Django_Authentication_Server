from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer(AbstractUser):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(
        max_length=255, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255)
    upazila = models.CharField(max_length=255)
    address = models.TextField()
    image = models.ImageField(
        upload_to='uploads/images/customer', blank=True, null=True)
    username = None

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f"{self.name}"

    def Image(self):
        if self.image:
            return mark_safe(
                '<img src="%s" alt="No Image" width="45" height="45" style="border-radius:10px" "/>' % self.image.url)
        return 'No Image'
    Image.short_description = 'Image'
