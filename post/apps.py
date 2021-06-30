from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PostConfig(AppConfig):
    name = 'post'
    verbose_name = _('Post')
