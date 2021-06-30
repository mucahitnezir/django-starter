from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CategoryConfig(AppConfig):
    name = 'category'
    verbose_name = _('Category')
