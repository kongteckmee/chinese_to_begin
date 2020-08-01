from django.contrib import admin
from .models import Store, Category

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description_1',
        'description_2',
        'description_3',
        'description_4',
        'before_discount',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
