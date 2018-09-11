from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from .models import Category


class CategoryAdmin(ExportActionModelAdmin):
    list_display = ['id', 'name', 'slug', 'type', 'published_at']
    list_filter = ['published_at', 'type']
    list_editable = ['name', 'type']
    search_fields = ['name', 'slug']
    pass


admin.site.register(Category, CategoryAdmin)
