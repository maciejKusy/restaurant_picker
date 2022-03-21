from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView

from restaurants.helpers import select_random_restaurant
from restaurants.models import Restaurant
from users.models import UserRestaurantPick


@login_required
def home_view(request):
    """
    Views the list of available restaurants to the user and a list of their picks for a given week. The template
    contains a 'pick restaurant' button so the logic for a POST request pertains to the creation of a
    UserRestaurantPick object.
    :param request: the HTTP request object.
    :return: renders the selected template and passes the necessary querysets to it.
    """
    current_week = timezone.now().isocalendar().week
    restaurant_list = list(Restaurant.objects.all())
    if request.method == "POST":
        if restaurant_list:
            random_restaurant = select_random_restaurant(
                request.user, restaurant_list, current_week
            )
            user_pick = UserRestaurantPick(
                user=request.user, restaurant=random_restaurant
            )
            user_pick.save()
            messages.success(
                request, f"{random_restaurant.name.title()} added to user picks list."
            )
        else:
            messages.info(request, f"There are no restaurants available!")

    current_week_picks = UserRestaurantPick.objects.all().filter(
        user=request.user, created_at_week_num=current_week
    )
    return render(
        request,
        "home.html",
        {"restaurants": restaurant_list, "weekly_picks": current_week_picks},
    )


class RestaurantCreationView(LoginRequiredMixin, CreateView):
    """
    Serves the purpose of creating a Restaurant object. Uses the out-of-the-box view to facilitate that.
    """
    model = Restaurant
    template_name = "restaurants/restaurant_create.html"
    fields = ["name", "url", "phone_number", "notes"]
    success_url = reverse_lazy("home")
