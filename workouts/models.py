from django.db import models


class Workout(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    one = models.TextField()
    two = models.TextField()
    three = models.TextField()
    four = models.TextField()
    five = models.TextField()
    six = models.TextField()
    seven = models.TextField()
    eight = models.TextField()
    nine = models.TextField()
    ten = models.TextField()
    image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)

    def __str__(self):
        return self.name
