from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import UpdateView

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


class ProfileEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = EditProfileForm
    template_name = 'account/edit-profile.html'
    success_url = reverse_lazy('account:edit-profile')
    success_message = _('Successful updating profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = _('Update Profile')
        return data
