from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, 'Logged in successfully')
        return redirect('home')

    context = {
        'form': form,
        'title': 'Giriş Yap'
    }
    return render(request, 'account/login.html', context)


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = True # Panele giriş yapabilmek için
        # user.is_superuser = True # Süper yetkili kullanıcı için
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        messages.success(request, 'Registered in successfully')
        return redirect('home')

    context = {
        'form': form,
        'title': 'Kayıt Ol'
    }
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('account:login')
