from django.contrib import admin
from .models import Workout


class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'image',
        'rating',
    )

    order = ('sku',)


admin.site.register(Workout, WorkoutAdmin)
