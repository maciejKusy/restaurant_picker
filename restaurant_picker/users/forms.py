from django.contrib.auth.forms import UserCreationForm, UsernameField

from users.models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
