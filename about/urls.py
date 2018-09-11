from django.conf.urls import url

from .views import *

app_name = 'about'

urlpatterns = [
    url(r'^$', about_index, name='index')
]
