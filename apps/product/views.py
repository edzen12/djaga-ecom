from django.shortcuts import render
# from django.views import generic ## ПЕРЕПИШИТЕ функции на КЛАССЫ, исп. ListView, DetailView
from django.db.models import Q

from apps.product.models import Product, Category, Images
from apps.home.models import Setting


def homepageview(request):
    categories = Category.objects.all()
    settings = Setting.objects.latest('id')
    if 'search_btn' in request.GET:
        key_word = request.GET.get('key_word')
        product_slider = Product.objects.filter(Q(title__icontains=key_word))
        return render(request, 'index.html', locals())
    product_slider = Product.objects.all() # товары для слайдера
    product_last = Product.objects.all().order_by('-id')[:4] # послдение добавленные товары
    product_random = Product.objects.all().order_by('?')[:4] # рандомные товары
    return render(request, 'index.html', locals())


def productdetail(request, slug):
    settings = Setting.objects.latest('id')
    product = Product.objects.get(slug=slug)
    images = Images.objects.filter(product=product)
    context = {
        'settings': settings,
        'product': product,
        'images': images
    }
    return render(request, 'home/product-page.html', context)
