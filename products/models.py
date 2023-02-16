from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    specification = models.TextField()
    description = models.TextField()
