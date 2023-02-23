from django.shortcuts import render
from products.models import Product


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': [
                {
                    'id': product.id,
                    'title': product.title,
                    'price': product.price,
                    'image': product.image,
                    'hashtags': product.hashtags.all()
                }
                for product in products
            ]
        }

        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all()
        }

        return render(request, 'products/detail.html', context=context)
