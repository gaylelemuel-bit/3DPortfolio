from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ('name', 'email', 'inquiry_type', 'subject', 'budget', 'timeline', 'submitted_at')
    list_filter     = ('inquiry_type', 'budget', 'timeline', 'heard_from', 'submitted_at')
    readonly_fields = ('name', 'email', 'inquiry_type', 'subject', 'budget', 'timeline', 'message', 'heard_from', 'submitted_at')
    ordering        = ('-submitted_at',)
