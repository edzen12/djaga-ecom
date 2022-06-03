from django.urls import path

from apps.product.views import homepageview, productdetail


urlpatterns = [
    path('', homepageview, name='homapage'),
    path('product/<slug:slug>/', productdetail, name='product_detail')
]
