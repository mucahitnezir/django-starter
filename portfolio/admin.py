from django.contrib import admin

from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'published_at', 'image')
    list_display_links = ('id',)
    list_editable = ('title', 'category')
    list_filter = ('published_at', 'category')
    search_fields = ('title', 'content')
