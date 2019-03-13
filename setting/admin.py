from django.contrib import admin

from .models import Setting


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('key', 'description', 'value')}),
    )
    list_display = ('id', 'key', 'description', 'admin_list_value', 'updated_at')
    list_filter = ('updated_at',)
    readonly_fields = ('key', 'description')
    search_fields = ('key', 'value')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
