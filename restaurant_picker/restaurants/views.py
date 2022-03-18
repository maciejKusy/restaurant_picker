from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from restaurants.models import Restaurant


class RestaurantCreationView(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = 'restaurants/restaurant_create.html'
    fields = ['name', 'url', 'phone_number', 'notes']
    success_url = reverse_lazy('home')
