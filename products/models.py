from django.db import models


class Hashtag(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    specification = models.TextField()
    description = models.TextField()
    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=455)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
