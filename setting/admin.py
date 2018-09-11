from django.contrib import admin
from .models import Setting


class SettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'description', 'admin_list_value', 'updated_at']
    search_fields = ['key', 'value']

    class Meta:
        model = Setting


admin.site.register(Setting, SettingAdmin)
