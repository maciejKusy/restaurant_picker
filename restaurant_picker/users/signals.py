from .models import User, UserRestaurantStack
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Ensures that a profile object is created upon creation of a new User object.
    """
    if created:
        UserRestaurantStack.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Ensures that a profile object is saved upon the respective User model being saved.
    """
    instance.restaurant_stack.save()
