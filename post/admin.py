from django.contrib import admin
from .models import Post, Comment, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'get_user', 'publishedAt']
    list_display_links = ['id']
    list_filter = ['publishedAt']
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


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'post_count', 'publishedAt']
    list_filter = ['publishedAt']
    list_editable = ['name']
    search_fields = ['name', 'slug']

    def post_count(self, obj):
        return len(obj.posts.all())

    post_count.short_description = 'İçerik Sayısı'

    class Meta:
        model = Category


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
