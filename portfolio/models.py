from django.db import models
from ckeditor.fields import RichTextField


# class Portfolio(models.Model):
#     title = models.CharField(max_length=120, verbose_name='Proje Adı')
#     slug = models.SlugField(max_length=120, verbose_name='Seo Url')
#     short_description = models.CharField(max_length=160, verbose_name='Kısa Açıklama')
#     content = models.TextField(verbose_name='Proje Açıklaması')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Proje'
#         verbose_name_plural = 'Projeler'
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=120, verbose_name='Kategori Adı')
#     slug = models.SlugField(unique=True, verbose_name='Slug', editable=False)
#     description = RichTextField(verbose_name='Kategori Açıklaması', null=True, blank=True)
#     meta_description = models.TextField(verbose_name='Meta Description', null=True, blank=True)
#     publishedAt = models.DateTimeField(verbose_name='Oluşturulma Tarihi', auto_now_add=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('post:category', kwargs={'slug': self.slug, 'id': self.id})
#
#     def get_posts_count(self):
#         return self.posts.count()
#
#     def get_unique_slug(self):
#         slug = slugify(self.name.replace('ı', 'i'))
#         unique_slug = slug
#         counter = 1
#         while Category.objects.filter(slug=unique_slug).exists():
#             unique_slug = "{}-{}".format(unique_slug, counter)
#             counter += 1
#         return unique_slug
#
#     def save(self, *args, **kwargs):
#         self.slug = self.get_unique_slug()
#         return super(Category, self).save(*args, **kwargs)
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = 'Kategori'
#         verbose_name_plural = 'Kategoriler'
