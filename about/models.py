from django.db import models
from django.utils.translation import ugettext_lazy as _


class TeamMember(models.Model):
    first_name = models.CharField(verbose_name=_('First Name'), max_length=100)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=100)
    title = models.CharField(verbose_name=_('Degree'), max_length=100)
    email_address = models.EmailField(verbose_name=_('Email Address'))
    linkedin_url = models.URLField(verbose_name=_('Linkedin Address'), null=True, blank=True)
    image = models.ImageField(verbose_name=_('Profile Photo'), null=True, blank=True)
    published_at = models.DateTimeField(verbose_name=_('Publishing Date'), auto_now_add=True, editable=False)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    full_name = property(get_full_name)

    class Meta:
        db_table = 'team_members'
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
