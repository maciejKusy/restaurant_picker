from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from restaurant_picker.constants import MAX_RESTAURANT_NAME_LENGTH, MAX_RESTAURANT_URL_LENGTH, \
    MAX_RESTAURANT_NOTES_LENGTH


class Restaurant(models.Model):
    name = models.CharField(max_length=MAX_RESTAURANT_NAME_LENGTH, null=False, blank=False)
    url = models.URLField(max_length=MAX_RESTAURANT_URL_LENGTH)
    phone_number = PhoneNumberField(blank=False)
    notes = models.TextField(max_length=MAX_RESTAURANT_NOTES_LENGTH)
