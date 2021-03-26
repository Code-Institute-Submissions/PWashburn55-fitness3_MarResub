from django.db import models


class Habit(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True,\
                              upload_to="./habits/static/habit-images")

    def __str__(self):
        return self.name
