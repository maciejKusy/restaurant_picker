from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class UserRestaurantStack(models.Model):
    user = models.OneToOneField(User, related_name="restaurant_stack", on_delete=models.CASCADE)
    weekly_restaurant_picks = models.ManyToManyField("restaurants.Restaurant", blank=True)

