from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class UserRestaurantPick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE, related_name='picks')
    created_at_week_num = models.IntegerField(default=timezone.now().isocalendar().week)

    def __str__(self):
        return f'{self.user.username}_{self.restaurant.name}_week:{self.created_at_week_num}'

