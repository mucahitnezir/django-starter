from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatechars

from ckeditor.fields import RichTextField


class Post(models.Model):
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, verbose_name=_('Post Category'),
                                 related_name='posts', limit_choices_to={'type': 'post'})
    user = models.ForeignKey('auth.User', verbose_name=_('Author'), on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=155, verbose_name=_('Post Title'))
    content = RichTextField(verbose_name=_('Post Content'))
    image = models.ImageField(null=True, blank=True, verbose_name=_('Post Picture'))
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name=_('Slug'), editable=False)
    published_at = models.DateTimeField(verbose_name=_('Publishing Date'), auto_now_add=True)

    @property
    def meta_description(self):
        return truncatechars(strip_tags(self.content), 160)

    class Meta:
        ordering = ['-published_at']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
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
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE, verbose_name=_('Post'))
    full_name = models.CharField(max_length=120, verbose_name=_('Full Name'))
    email_address = models.CharField(max_length=60, verbose_name=_('Email Address'))
    content = models.TextField(verbose_name=_('Comment'))
    is_confirmed = models.BooleanField(verbose_name=_('Approval Status'), default=False)
    published_at = models.DateTimeField(verbose_name=_('Publishing Date'), auto_now_add=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        db_table = 'comments'

    def __str__(self):
        return "{} - {}".format(self.id, self.full_name)
