from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'get_user', 'publishedAt']
    list_display_links = ['id']
    list_filter = ['publishedAt', 'category']
    search_fields = ['title', 'content']
    list_editable = ['title']

    def get_user(self, obj):
        return obj.user.get_full_name()

    get_user.admin_order_field = 'user'  # Allows column order sorting
    get_user.short_description = 'Yazar'  # Renames column head

    class Meta:
        model = Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email_address', 'get_post', 'publishedAt', 'is_confirmed']
    list_filter = ['is_confirmed', 'post']
    list_editable = ['is_confirmed']
    search_fields = ['full_name', 'email_address', 'content']

    def get_post(self, obj):
        return obj.post.title

    get_post.admin_order_field = 'post'
    get_post.short_description = 'İçerik'

    class Meta:
        model = Comment


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
