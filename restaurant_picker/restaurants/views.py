from random import randint

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from restaurants.models import Restaurant
from users.models import UserRestaurantPick


def determine_if_userpicks_full(user):
    number_of_restaurants = len(Restaurant.objects.all())
    number_of_user_picks = len(UserRestaurantPick.objects.all().filter(user=user))
    if number_of_restaurants <= number_of_user_picks:
        return True
    return False


def select_random_restaurant(user, restaurant_list):
    restaurant_number = len(restaurant_list)
    random_restaurant = restaurant_list[randint(0, (restaurant_number - 1))]
    picks_full_flag = determine_if_userpicks_full(user)
    print(picks_full_flag)
    if picks_full_flag:
        return random_restaurant
    else:
        if random_restaurant.picks.all():
            return select_random_restaurant(user, restaurant_list)
        else:
            return random_restaurant


@login_required
def home_view(request):
    restaurant_list = list(Restaurant.objects.all())
    if request.method == "POST":
        if restaurant_list:
            random_restaurant = select_random_restaurant(request.user, restaurant_list)
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
