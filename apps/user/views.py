from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages

from apps.user.forms import UserForm, LoginForm

User = get_user_model()


def user_register_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('homepage')
    return render(request, 'user/register.html', {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('homepage')
            except:
                messages.error(request, 'Не правильный логин или пароль')
    form = LoginForm()
    return render(request, 'user/login.html', {'form': form})
