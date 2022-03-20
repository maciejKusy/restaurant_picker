from django.contrib.auth.forms import UserCreationForm, UsernameField
from users.models import User


class UserRegistrationForm(UserCreationForm):
    """
    Serves the purpose of registering a new user account - uses the generic form for that.
    """
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
