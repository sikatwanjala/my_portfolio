from django.contrib import admin
from .models import Document

admin.site.register(Document)

from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'subject',
        'created_at'
    )

    search_fields = (
        'name',
        'email',
        'subject'
    )

    list_filter = (
        'created_at',
    )