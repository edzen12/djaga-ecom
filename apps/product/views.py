from django.shortcuts import render
# from django.views import generic

from apps.product.models import Product, Category


def homepageview(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})
