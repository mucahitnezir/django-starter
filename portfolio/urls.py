from django.conf.urls import url
from .views import *

app_name = 'portfolio'

urlpatterns = [
    url(r'^$', portfolio_index, name='index'),
    url('^(?P<slug>[\w-]+)/$', portfolio_detail, name='detail'),
]
