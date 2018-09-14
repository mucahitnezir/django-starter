from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField


CATEGORY_TYPES = (
    ('post', _('Post Category')),
    ('portfolio', _('Portfolio Category')),
    ('service', _('Service Category')),
)


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Category Name'))
    slug = models.SlugField(unique=True, verbose_name=_('Slug'), editable=False)
    type = models.CharField(max_length=9, verbose_name=_('Category Type'), choices=CATEGORY_TYPES, default='post')
    description = RichTextField(verbose_name=_('Category Description'), null=True, blank=True)
    meta_description = models.TextField(verbose_name=_('Meta Description'), null=True, blank=True)
    published_at = models.DateTimeField(verbose_name=_('Publishing Date'), auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        db_table = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:category', kwargs={'slug': self.slug, 'id': self.id})

    def get_posts_count(self):
        return self.posts.count()

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(unique_slug, counter)
            counter += 1
        return unique_slug
