from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email_address', 'subject', 'published_at']
    list_filter = ['published_at']
    search_fields = ['first_name', 'last_name', 'email_address', 'subject', 'message']

    class Meta:
        model = Message

    def has_change_permission(self, request, obj=None):
        return False
