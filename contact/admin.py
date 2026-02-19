from django.contrib import admin
from contact.models import Message


# Message Admin Configuration
# Customizes how contact messages appear in Django Admin

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    # Fields displayed in admin list view
    list_display = [
        'id',
        'name',
        'email',
        'subject',
        'message',
        'updated_date',
        'created_date'
    ]

    # Enables search functionality in admin panel
    search_fields = ['name', 'email', 'subject', 'message']

    class Meta:
        model = Message