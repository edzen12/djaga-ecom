from django.shortcuts import render
# from django.views import generic
from django.db.models import Q

from apps.product.models import Product, Category, Images


def homepageview(request):
    categories = Category.objects.all()
    if 'search_btn' in request.GET:
        key_word = request.GET.get('key_word')
        product_slider = Product.objects.filter(Q(title__icontains=key_word))
        return render(request, 'index.html', locals())
    product_slider = Product.objects.all()
    return render(request, 'index.html', locals())


def productdetail(request, slug):
    product = Product.objects.get(slug=slug)
    images = Images.objects.filter(product=product)
    context = {
        'product': product,
        'images': images
    }
    return render(request, 'home/product-page.html', context)
