from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatechars

from ckeditor.fields import RichTextField


class Post(models.Model):
    category = models.ForeignKey(
        to='category.Category',
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name=_('Post Category'),
        limit_choices_to={'type': 'post'}
    )
    user = models.ForeignKey('auth.User', models.CASCADE, 'posts', verbose_name=_('Author'))
    title = models.CharField(_('Post Title'), max_length=155)
    slug = models.SlugField(_('Slug'), unique=True, null=True, blank=True)
    content = RichTextField(_('Post Content'))
    image = models.ImageField(_('Post Picture'), null=True, blank=True)
    published_at = models.DateTimeField(_('Publishing Date'), auto_now_add=True)

    @property
    def meta_description(self):
        return truncatechars(strip_tags(self.content), 160)

    class Meta:
        db_table = 'posts'
        ordering = ('-published_at',)
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

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
        if not self.slug:
            slug = slugify(self.title.replace('ı', 'i'))
            unique_slug = slug
            counter = 1
            while Post.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = "{}-{}".format(unique_slug, counter)
                counter += 1
            return unique_slug
        else:
            return self.slug


class Comment(models.Model):
    post = models.ForeignKey('post.Post', models.CASCADE, 'comments', verbose_name=_('Post'))
    full_name = models.CharField(_('Full Name'), max_length=120)
    email_address = models.CharField(_('Email Address'), max_length=60)
    content = models.TextField(_('Comment'))
    is_confirmed = models.BooleanField(_('Approval Status'), default=False)
    published_at = models.DateTimeField(_('Publishing Date'), auto_now_add=True)

    class Meta:
        db_table = 'comments'
        ordering = ('-published_at',)
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return "{} - {}".format(self.id, self.full_name)
