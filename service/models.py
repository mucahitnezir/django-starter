from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify


class Service(models.Model):
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='services',
                                 verbose_name='Hizmet Kategorisi', limit_choices_to={'type': 'service'})
    title = models.CharField(max_length=160, verbose_name='Hizmet Adı')
    slug = models.SlugField(unique=True, verbose_name='Slug', editable=False)
    short_description = models.TextField(verbose_name='Kısa Açıklama')
    meta_description = models.TextField(verbose_name='Meta Açıklama')
    content = RichTextField(verbose_name='Hizmet İçeriği')
    image = models.ImageField(verbose_name='Hizmet Görseli')
    published_at = models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'
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
