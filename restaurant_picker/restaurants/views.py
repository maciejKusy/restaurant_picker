from random import randint

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from restaurants.models import Restaurant
from users.models import UserRestaurantPick

# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = 'home.html'


@login_required
def home_view(request):
    restaurant_list = list(Restaurant.objects.all())
    if request.method == "POST":
        if restaurant_list:
            restaurant_number = len(restaurant_list)
            random_restaurant = restaurant_list[randint(0, (restaurant_number - 1))]
            user_pick = UserRestaurantPick(user=request.user, restaurant=random_restaurant)
            user_pick.save()
            messages.success(request, f'{random_restaurant.name} added to user picks list.')
        else:
            messages.info(request, f'There are no restaurants available!')

    return render(request, 'home.html', {'restaurants': restaurant_list})


class RestaurantCreationView(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = 'restaurants/restaurant_create.html'
    fields = ['name', 'url', 'phone_number', 'notes']
    success_url = reverse_lazy('home')
