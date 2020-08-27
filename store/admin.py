from django.contrib import admin
from .models import Store, Condition


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


class ConditionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Store, StoreAdmin)
admin.site.register(Condition, ConditionAdmin)
