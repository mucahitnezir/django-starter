from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'published_at', 'image']
    list_display_links = ['id']
    list_filter = ['published_at', 'category']
    search_fields = ['title', 'content']
    list_editable = ['title']

    class Meta:
        model = Portfolio


admin.site.register(Portfolio, PortfolioAdmin)
