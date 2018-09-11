from django.conf.urls import url
from .views import *

app_name = 'contact'

urlpatterns = [
    url(r'^$', contact_index, name='index')
]
