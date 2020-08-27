from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    readonly_fields = ['date_created']

    fieldsets = [
        ('Message Detail', {'fields': ['email', 'name', 'message']}),
        ('Admin', {'fields': ['date_created', ]}),
    ]

    list_display = (
        'name',
        'email',
        'message',
        'date_created',
    )

    list_filter = ['date_created']


admin.site.register(Contact, ContactAdmin)
