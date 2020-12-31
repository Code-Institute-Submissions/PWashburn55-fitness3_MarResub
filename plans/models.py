from django.db import models


class Plan(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    A = models.TextField()
    B = models.TextField()
    C = models.TextField()
    D = models.TextField()
    E = models.TextField()
    F = models.TextField()
    G = models.TextField()
    H = models.TextField()
    I = models.TextField()
    J = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name