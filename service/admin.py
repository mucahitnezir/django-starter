from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'published_at')
    list_editable = ('title', 'category')
    list_filter = ('published_at', 'category')
    search_fields = ('title', 'slug', 'short_description', 'meta_description', 'content')
