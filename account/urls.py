from django.urls import path
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'account'

urlpatterns = [
    path(_('login/'), auth_views.LoginView.as_view(template_name="account/login.html"), name='login'),
    path(_('register/'), register_view, name='register'),
    path(_('logout/'), auth_views.LogoutView.as_view(), name='logout'),
    path(_('edit-profile/'), profile_edit_view, name='edit-profile'),
]
