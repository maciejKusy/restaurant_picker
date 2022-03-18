from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class UserRestaurantPick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


