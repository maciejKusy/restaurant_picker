from random import randint

from restaurants.models import Restaurant
from users.models import UserRestaurantPick


def select_random_restaurant(user, restaurant_list, current_week):
    """
    Selects one of the available restaurants at random. Prevents choosing a restaurant that has already been chosen in
    a given week until all restaurants have been chosen. After that, picks can be duplicated.
    :param user: the instance of User model for a given request.
    :param restaurant_list: a list of all the Restaurant objects in the database.
    :param current_week: the week number corresponding to the current date.
    :return: a Restaurant object.
    """
    restaurant_number = len(restaurant_list)
    random_restaurant = restaurant_list[randint(0, (restaurant_number - 1))]
    picks_full_flag = determine_if_userpicks_full(user, current_week)
    if picks_full_flag:
        return random_restaurant
    else:
        if random_restaurant.picks.all().filter(
            user=user, created_at_week_num=current_week
        ):
            return select_random_restaurant(user, restaurant_list, current_week)
        else:
            return random_restaurant


def determine_if_userpicks_full(user, current_week):
    """
    Checks whether the user has added all available restaurants to their picks by comparing the length of the list the
    user's picks for a given week with the list of all restaurants. Seeing as the function select_random_restaurant
    prevents adding a duplicated pick, the flag should only change once all available restaurants have been picked
    in a given week.
    :param user: the instance of User model for a given request.
    :param current_week: the week number corresponding to the current date.
    :return: a boolean True or False.
    """
    number_of_restaurants = len(Restaurant.objects.all())
    number_of_user_picks = len(
        UserRestaurantPick.objects.all().filter(
            user=user, created_at_week_num=current_week
        )
    )
    if number_of_restaurants <= number_of_user_picks:
        return True
    return False