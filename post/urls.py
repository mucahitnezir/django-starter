from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import *

app_name = 'post'

urlpatterns = [
    url(r'^$', post_index, name='index'),
    url(_('^create/$'), post_create, name='create'),
    url('^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(_('^(?P<id>\d+)/update$'), post_update, name='update'),
    url(_('^(?P<id>\d+)/delete$'), post_delete, name='delete'),
    url('^c/(?P<slug>[\w-]+)-(?P<id>\d+)$', category_detail, name='category')
]
