from django.conf.urls import url
from .views import *

app_name = 'service'

urlpatterns = [
    url(r'^$', service_index, name='index'),
    url('^(?P<slug>[\w-]+)/$', service_detail, name='detail'),
]
