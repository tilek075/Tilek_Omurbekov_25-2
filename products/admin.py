from django.contrib import admin
from products.models import Product, Hashtag, Review

admin.site.register(Product)
admin.site.register(Hashtag)
admin.site.register(Review)
