from django.urls import path

from apps.product.views import homepageview, productdetail


urlpatterns = [
    path('', homepageview, name='homepage'),
    path('product/<slug:slug>/', productdetail, name='product_detail')
]
