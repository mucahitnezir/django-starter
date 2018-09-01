from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'publishedAt']
    list_editable = ['title', 'category']
    search_fields = ['title', 'slug', 'short_description', 'meta_description', 'content']
    list_filter = ['publishedAt', 'category']

    class Meta:
        model = Service


admin.site.register(Service, ServiceAdmin)
