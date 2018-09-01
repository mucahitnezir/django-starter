from django.conf.urls import url
from .views import *

app_name = 'service'

urlpatterns = [
    url('^index/$', service_index, name='index'),
    url('^(?P<slug>[\w-]+)/$', service_detail, name='detail'),
]
