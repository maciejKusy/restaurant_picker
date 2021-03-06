from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from restaurant_picker.constants import (MAX_RESTAURANT_NAME_LENGTH,
                                         MAX_RESTAURANT_NOTES_LENGTH,
                                         MAX_RESTAURANT_URL_LENGTH)


class Restaurant(models.Model):
    """
    Stores information on individual restaurants.
    """
    name = models.CharField(
        max_length=MAX_RESTAURANT_NAME_LENGTH, unique=True, null=False, blank=False
    )
    url = models.URLField(max_length=MAX_RESTAURANT_URL_LENGTH)
    phone_number = PhoneNumberField(blank=False)
    notes = models.TextField(max_length=MAX_RESTAURANT_NOTES_LENGTH)

    def __str__(self):
        return self.name
