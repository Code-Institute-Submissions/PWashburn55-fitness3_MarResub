from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserPoints(models.Model, UserProfile):
    """ user profile model for maintaining user points """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username.UserPoints


@receiver(post_save, sender=User)
def update_user_points(sender, instance, **kwargs):
    instance.UserPoints.save()





