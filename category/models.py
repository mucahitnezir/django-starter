from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField


CATEGORY_TYPES = (
    ('post', _('Post Category')),
    ('portfolio', _('Portfolio Category')),
    ('service', _('Service Category')),
)


class Category(models.Model):
    name = models.CharField(_('Category Name'), max_length=120)
    slug = models.SlugField(_('Slug'), unique=True, blank=True)
    type = models.CharField(_('Category Type'), max_length=9, choices=CATEGORY_TYPES, default='post')
    description = RichTextField(_('Category Description'), null=True, blank=True)
    meta_description = models.TextField(_('Meta Description'), null=True, blank=True)
    published_at = models.DateTimeField(_('Publishing Date'), auto_now_add=True)

    class Meta:
        db_table = 'categories'
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug, 'id': self.id})

    def get_posts_count(self):
        return self.posts.count()
