from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.user.views import user_register_view, user_login_view


urlpatterns = [
    path('register/', user_register_view, name='user_register'),
    path('login/', user_login_view, name='user_login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout')
]
