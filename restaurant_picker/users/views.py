from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegistrationForm


class HomeView(TemplateView):
    template_name = 'home.html'


class UserRegistrationView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    success_url = '/login/'
    form_class = UserRegistrationForm
    success_message = "Account created!"
