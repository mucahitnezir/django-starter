from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'get_user', 'published_at')
    list_display_links = ('id',)
    list_editable = ('title', 'category')
    list_filter = ('published_at', 'category')
    search_fields = ('title', 'content')

    def get_user(self, obj):
        return obj.user.get_full_name()

    get_user.admin_order_field = 'user'  # Allows column order sorting
    get_user.short_description = _('Author')  # Renames column head


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email_address', 'get_post', 'published_at', 'is_confirmed')
    list_editable = ('is_confirmed',)
    list_filter = ('is_confirmed', 'post')
    search_fields = ('full_name', 'email_address', 'content')

    def get_post(self, obj):
        return obj.post.title

    get_post.admin_order_field = 'post'
    get_post.short_description = _('Post')
