from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'user', 'published_at')
    list_display_links = ('id',)
    list_filter = ('published_at', 'category')
    list_select_related = ('category', 'user')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category__name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email_address', 'post', 'published_at', 'is_confirmed')
    list_editable = ('is_confirmed',)
    list_filter = ('is_confirmed', 'post')
    list_select_related = ('post',)
    search_fields = ('full_name', 'email_address', 'content')
