from django.urls import path

from apps.product.views import homepageview


urlpatterns = [
    path('', homepageview, name='homapage'),
]
