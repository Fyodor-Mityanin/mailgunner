from django.contrib import admin

from .models import Email, SentMail

class EmailAdmin(admin.ModelAdmin):
    """Админка для базы e-mail"""
    list_display = (
        'email',
        'name',
        'surname',
        'birth_date',
    )
    search_fields = ('email',)
    list_filter = ('birth_date',)
    empty_value_display = '-пусто-'

class SentMailAdmin(admin.ModelAdmin):
    """Админка для отправленных e-mail"""
    list_display = (
        'email',
        'send_date',
        'is_read',
    )
    search_fields = ('email',)
    list_filter = ('send_date',)
    empty_value_display = '-пусто-'

admin.site.register(Email, EmailAdmin)
admin.site.register(SentMail, SentMailAdmin)
