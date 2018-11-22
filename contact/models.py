from django.db import models
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    email_address = models.EmailField(verbose_name=_('Email Address'))
    subject = models.CharField(max_length=255, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Your Message'))
    published_at = models.DateTimeField(verbose_name=_('Publishing Date'), auto_now_add=True)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    full_name = property(get_full_name)

    class Meta:
        ordering = ['-id']
        db_table = 'messages'
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def __str__(self):
        return self.subject
