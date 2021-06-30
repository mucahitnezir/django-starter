from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class LandingConfig(AppConfig):
    name = 'landing'
    verbose_name = _('Landing')
