from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField


class Portfolio(models.Model):
    category = models.ForeignKey(
        to='category.Category',
        on_delete=models.CASCADE,
        related_name='portfolios',
        verbose_name=_('Portfolio Category'),
        limit_choices_to={'type': 'portfolio'}
    )
    title = models.CharField(_('Portfolio Title'), max_length=120)
    slug = models.SlugField(_('Slug'), unique=True, blank=True)
    short_description = models.TextField(_('Meta Description'))
    content = RichTextField(_('Portfolio Description'))
    image = models.ImageField(_('Portfolio Image'), null=True, blank=True)
    published_at = models.DateTimeField(_('Publishing Date'), auto_now_add=True)

    class Meta:
        db_table = 'portfolios'
        ordering = ('-published_at',)
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolios')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Portfolio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio:detail', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        if not self.slug:
            slug = slugify(self.title.replace('ı', 'i'))
            unique_slug = slug
            counter = 1
            while Portfolio.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = "{}-{}".format(unique_slug, counter)
                counter += 1
            return unique_slug
        else:
            return self.slug
