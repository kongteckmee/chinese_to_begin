from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'order_total',)
    fields = ('order_number', 'date', 'full_name', 
            'email', 'phone_number', 'country', 'postcode', 
            'town_or_city', 'street_address_1', 'street_address_2', 
            'county', 'order_total',)
    
    list_display = ('order_number', 'date', 'full_name',
                    'email', 'phone_number', 'order_total',)
    
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
