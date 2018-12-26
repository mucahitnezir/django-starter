from django.urls import path
from django.utils.translation import ugettext_lazy as _

from .views import *

app_name = 'post'

urlpatterns = [
    path('', post_index, name='index'),
    path(_('create/'), post_create, name='create'),
    path('<slug>/', post_detail, name='detail'),
    path(_('<id>/update/'), post_update, name='update'),
    path(_('<id>/delete/'), post_delete, name='delete'),
    path('c/<slug>-<id>/', category_detail, name='category')
]
