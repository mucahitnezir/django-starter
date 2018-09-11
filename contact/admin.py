from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email_address', 'phone_number', 'subject', 'published_at']
    search_fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'subject', 'message']
    list_filter = ['published_at']

    class Meta:
        model = Message


admin.site.register(Message, MessageAdmin)
