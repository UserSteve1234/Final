from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Publications(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250) 
    author_of_publication = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        ordering = ['-created_at']

   