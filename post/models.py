from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Post(models.Model):
    category = models.ForeignKey('post.Category', on_delete=models.CASCADE, verbose_name='Kategori', related_name='posts')
    user = models.ForeignKey('auth.User', verbose_name='Yazar', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=155, verbose_name='Başlık')
    content = RichTextField(verbose_name='İçerik')
    publishedAt = models.DateTimeField(verbose_name='Yayın Tarihi', auto_now_add=True)
    image = models.ImageField(null=True, blank=True, verbose_name='Resim')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='Slug', editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/post/{}".format(self.id)
        return reverse('post:detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(unique_slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishedAt']
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'


class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE, verbose_name='İçerik')
    full_name = models.CharField(max_length=120, verbose_name='Ad Soyad')
    email_address = models.CharField(max_length=60, verbose_name='E-Posta Adresi')
    content = models.TextField(verbose_name='Yorum')
    is_confirmed = models.BooleanField(verbose_name='Onay Durumu', default=False)
    publishedAt = models.DateTimeField(verbose_name='Yorum Tarihi', auto_now_add=True)

    class Meta:
        ordering = ['-publishedAt']
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name='Kategori Adı')
    slug = models.SlugField(unique=True, verbose_name='Slug', editable=False)
    description = RichTextField(verbose_name='Kategori Açıklaması', null=True, blank=True)
    meta_description = models.TextField(verbose_name='Meta Description', null=True, blank=True)
    publishedAt = models.DateTimeField(verbose_name='Oluşturulma Tarihi', auto_now_add=True)

    def __str__(self):
        return self.name

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

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
