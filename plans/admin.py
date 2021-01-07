from django.contrib import admin
from .models import Plan


class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'rating',
        'image'
    )

    order = ('sku',)


admin.site.register(Plan, PlanAdmin)
