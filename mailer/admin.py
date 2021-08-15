from django.contrib import admin

from .models import Email, EmailTemplate, SentEmail


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


class SentEmailAdmin(admin.ModelAdmin):
    """Админка для отправленных e-mail"""
    list_display = (
        'pk',
        'email',
        'template',
        'send_date',
        'is_read',
    )
    search_fields = ('email',)
    list_filter = ('send_date',)
    empty_value_display = '-пусто-'


class EmailTemplateAdmin(admin.ModelAdmin):
    """Админка для базы шаблонов e-mail"""
    list_display = (
        'title',
        'subject',
        'link',
    )


admin.site.register(Email, EmailAdmin)
admin.site.register(SentEmail, SentEmailAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
