from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'sku' ,
        'name' ,
        'description_1' ,
        'description_2' ,
        'description_3' ,
        'description_4' ,
        'price' ,
        'image' ,
    )

    ordering = ('sku',)

admin.site.register(Course, CourseAdmin)
