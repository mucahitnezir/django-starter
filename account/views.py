from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import UpdateView, CreateView

from .forms import RegisterForm, EditProfileForm


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('landing:home')
    success_message = _('Successful signup')
    extra_context = {'title': _('Signup')}

    def form_valid(self, form):
        # Create user row
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = True
        # user.is_superuser = True
        user.save()
        # Login
        new_user = authenticate(username=user.username, password=password)
        login(self.request, new_user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Üyelik kaydı oluşturulamadı')
        return super().form_invalid(form)


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
