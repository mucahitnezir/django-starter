from django.urls import path
from django.utils.translation import ugettext_lazy as _

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, CategoryDetailView, post_delete

app_name = 'post'

urlpatterns = (
    path('', PostListView.as_view(), name='index'),
    path(_('create/'), PostCreateView.as_view(), name='create'),
    path('<slug>/', PostDetailView.as_view(), name='detail'),
    path(_('<id>/update/'), PostUpdateView.as_view(), name='update'),
    path(_('<id>/delete/'), post_delete, name='delete'),
    path('c/<slug>-<id>/', CategoryDetailView.as_view(), name='category')
)
