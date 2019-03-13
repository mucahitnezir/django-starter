from django.contrib import admin

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'title', 'email_address', 'published_at')
    list_editable = ('title', 'email_address')
    list_filter = ('published_at', 'title')
    search_fields = ('first_name', 'last_name', 'email_address', 'title')
