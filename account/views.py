from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from .forms import RegisterForm, EditProfileForm


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
        messages.success(request, _('Successful signup'))
        return redirect('home')

    context = {
        'form': form,
        'title': _('Signup')
    }
    return render(request, 'account/register.html', context)


@login_required
def profile_edit_view(request):
    form = EditProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, _('Successful updating profile'))

    context = {
        'title': _('Update Profile'),
        'form': form
    }

    return render(request, 'account/edit-profile.html', context)
