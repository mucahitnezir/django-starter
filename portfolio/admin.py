from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'publishedAt', 'image']
    list_display_links = ['id']
    list_filter = ['publishedAt', 'category']
    search_fields = ['title', 'content']
    list_editable = ['title']

    class Meta:
        model = Portfolio


admin.site.register(Portfolio, PortfolioAdmin)
