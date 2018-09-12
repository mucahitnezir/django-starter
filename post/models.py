from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import strip_tags
from django.template.defaultfilters import truncatechars

from ckeditor.fields import RichTextField


class Post(models.Model):
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, verbose_name='Kategori',
                                 related_name='posts', limit_choices_to={'type': 'post'})
    user = models.ForeignKey('auth.User', verbose_name='Yazar', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=155, verbose_name='Başlık')
    content = RichTextField(verbose_name='İçerik')
    image = models.ImageField(null=True, blank=True, verbose_name='Resim')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='Slug', editable=False)
    published_at = models.DateTimeField(verbose_name='Yayın Tarihi', auto_now_add=True)

    @property
    def meta_description(self):
        return truncatechars(strip_tags(self.content), 160)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'
        db_table = 'posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return "/post/{}".format(self.id)
        return reverse('post:detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})

    def get_confirmed_comments(self):
        return self.comments.filter(is_confirmed=True)

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(unique_slug, counter)
            counter += 1
        return unique_slug


class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE, verbose_name='İçerik')
    full_name = models.CharField(max_length=120, verbose_name='Ad Soyad')
    email_address = models.CharField(max_length=60, verbose_name='E-Posta Adresi')
    content = models.TextField(verbose_name='Yorum')
    is_confirmed = models.BooleanField(verbose_name='Onay Durumu', default=False)
    published_at = models.DateTimeField(verbose_name='Yorum Tarihi', auto_now_add=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
        db_table = 'comments'

    def __str__(self):
        return "{} - {}".format(self.id, self.full_name)
