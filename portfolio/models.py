from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Portfolio(models.Model):
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='portfolios',
                                 verbose_name='Proje Kategorisi')
    title = models.CharField(max_length=120, verbose_name='Proje Adı')
    slug = models.SlugField(unique=True, verbose_name='Slug', editable=False)
    short_description = models.TextField(verbose_name='Meta Description')
    content = RichTextField(verbose_name='Proje Açıklaması')
    image = models.ImageField(null=True, blank=True, verbose_name='Proje Görseli')
    published_at = models.DateTimeField(verbose_name='Proje Yayınlanma Tarihi', auto_now_add=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'
        db_table = 'portfolios'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Portfolio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('portfolio:detail', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Portfolio.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(unique_slug, counter)
            counter += 1
        return unique_slug
