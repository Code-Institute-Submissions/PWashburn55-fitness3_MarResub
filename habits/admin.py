from django.contrib import admin
from .models import Habit


class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Habit, HabitAdmin)

