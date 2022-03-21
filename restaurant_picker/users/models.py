from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Stores the basic information pertaining to a user. No customization for now but overridden as per the framework
    documentation in order to accommodate any future changes.
    """
    pass

    def __str__(self):
        return self.username


class UserRestaurantPick(models.Model):
    """
    A UserRestaurantPick object represents the action of adding a restaurant to one's recommendations list by a user.
    The model therefore contains references both to the User and Restaurant models and a timestamp relevant to the
    site logic.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        "restaurants.Restaurant", on_delete=models.CASCADE, related_name="picks"
    )
    created_at_week_num = models.IntegerField(
        MinValueValidator(1),
        MaxValueValidator(53),
        default=timezone.now().isocalendar().week
    )

    def __str__(self):
        return f"{self.user.username}_{self.restaurant.name}_week:{self.created_at_week_num}"
