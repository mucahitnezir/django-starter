from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import views as auth_views

from .views import *


app_name = 'account'

urlpatterns = [
    url(_(r'^login$'), auth_views.LoginView.as_view(template_name="account/login.html"), name='login'),
    url(_(r'^register$'), register_view, name='register'),
    url(_(r'^logout$'), auth_views.LogoutView.as_view(), name='logout'),
    url(_(r'^edit-profile$'), profile_edit_view, name='edit-profile'),
]
