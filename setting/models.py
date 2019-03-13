from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import ugettext_lazy as _


class Setting(models.Model):
    key = models.CharField(_('Parameter'), max_length=32, unique=True, editable=False)
    description = models.CharField(_('Parameter Description'), max_length=255, null=True, blank=True)
    value = models.TextField(_('Parameter Value'), null=True, blank=True)
    updated_at = models.DateTimeField(_('Last Updated Date'), auto_now=True, null=True, blank=True)

    @property
    def admin_list_value(self):
        return truncatechars(self.value, 100)

    class Meta:
        db_table = 'settings'
        ordering = ('key',)
        verbose_name = _('Parameter')
        verbose_name_plural = _('Parameters')

    def __str__(self):
        return self.key

    @staticmethod
    def get_one(key, return_type='value'):
        # Find setting
        setting = Setting.objects.get(key=key)
        # Return setting
        if return_type == 'value':
            return setting.value
        elif return_type == 'full':
            return setting
        else:
            return None

    @staticmethod
    def get_multiple(keys):
        result = {}
        settings = Setting.objects.filter(key__in=keys)
        for setting in settings:
            result[setting.key] = setting.value
        return result
