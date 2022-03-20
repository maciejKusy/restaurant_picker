from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from users.forms import UserRegistrationForm


class UserRegistrationView(SuccessMessageMixin, CreateView):
    """
    Serves the purpose of registering new user accounts.
    """
    template_name = "users/register.html"
    success_url = "/login/"
    form_class = UserRegistrationForm
    success_message = "Account created!"


class UserLoginView(LoginView):
    """
    Serves the purpose of logging into a user account.
    """
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    """
    The basic view initiated upon logging out.
    """
    template_name = "users/logout.html"
