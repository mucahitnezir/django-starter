from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField


class Service(models.Model):
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='services',
                                 verbose_name=_('Service Category'), limit_choices_to={'type': 'service'})
    title = models.CharField(max_length=160, verbose_name=_('Service Name'))
    slug = models.SlugField(unique=True, verbose_name=_('Slug'), editable=False)
    short_description = models.TextField(verbose_name=_('Short Description'))
    meta_description = models.TextField(verbose_name=_('Meta Description'))
    content = RichTextField(verbose_name=_('Service Content'))
    image = models.ImageField(verbose_name=_('Service Picture'))
    published_at = models.DateTimeField(verbose_name=_('Publishing Date'), auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        db_table = 'services'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Service, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service:detail', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Service.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(unique_slug, counter)
            counter += 1
        return unique_slug
