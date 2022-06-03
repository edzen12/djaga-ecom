from django.shortcuts import render
# from django.views import generic

from apps.product.models import Product, Category, Images


def homepageview(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def productdetail(request, slug):
    product = Product.objects.get(slug=slug)
    images = Images.objects.filter(product=product)
    context = {
        'product': product,
        'images': images
    }
    return render(request, 'home/product-page.html', context)
