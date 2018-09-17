from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from .views import *


app_name = 'account'

urlpatterns = [
    url(_(r'^login$'), login_view, name='login'),
    url(_(r'^register$'), register_view, name='register'),
    url(_(r'^logout$'), logout_view, name='logout'),
    url(_(r'^edit-profile$'), profile_edit_view, name='edit-profile'),
]
