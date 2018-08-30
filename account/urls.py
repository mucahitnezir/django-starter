from django.conf.urls import url
from .views import *


app_name = 'account'

urlpatterns = [
    url(r'^login$', login_view, name='login'),
    url(r'^register$', register_view, name='register'),
    url(r'^logout', logout_view, name='logout'),
    url(r'^edit-profile', profile_edit_view, name='edit-profile'),
]
