from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


CATEGORY_TYPES = (
    ('post', 'Blog Kategorisi'),
    ('portfolio', 'Portfolyo Kategorisi'),
    ('service', 'Hizmet Kategorisi'),
)


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name='Kategori Adı')
    slug = models.SlugField(unique=True, verbose_name='Slug', editable=False)
    type = models.CharField(max_length=9, verbose_name='Kategori Tipi', choices=CATEGORY_TYPES, default='post')
    description = RichTextField(verbose_name='Kategori Açıklaması', null=True, blank=True)
    meta_description = models.TextField(verbose_name='Meta Description', null=True, blank=True)
    published_at = models.DateTimeField(verbose_name='Oluşturulma Tarihi', auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
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
