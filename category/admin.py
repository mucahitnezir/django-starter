from django.contrib import admin
from import_export.admin import ExportActionModelAdmin
from .models import Category


@admin.register(Category)
class CategoryAdmin(ExportActionModelAdmin):
    list_display = ('id', 'name', 'slug', 'type', 'published_at')
    list_editable = ('name', 'type')
    list_filter = ('published_at', 'type')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
