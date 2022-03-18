from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegistrationForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class UserRegistrationView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    success_url = '/login/'
    form_class = UserRegistrationForm
    success_message = "Account created!"


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
