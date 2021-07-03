from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField


class Service(models.Model):
    category = models.ForeignKey(
        to='category.Category',
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name=_('Service Category'),
        limit_choices_to={'type': 'service'}
    )
    title = models.CharField(_('Service Name'), max_length=160)
    slug = models.SlugField(_('Slug'), unique=True, blank=True)
    short_description = models.TextField(_('Short Description'))
    meta_description = models.TextField(_('Meta Description'))
    content = RichTextField(_('Service Content'))
    image = models.ImageField(_('Service Picture'))
    published_at = models.DateTimeField(_('Publishing Date'), auto_now_add=True)

    class Meta:
        db_table = 'services'
        ordering = ('title',)
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service:detail', kwargs={'slug': self.slug})
