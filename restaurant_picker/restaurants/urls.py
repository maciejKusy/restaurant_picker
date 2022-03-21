from django.urls import path
from restaurants.views import home_view, RestaurantCreationView

urlpatterns = [
    path("", home_view, name="home"),
    path("create-restaurant/", RestaurantCreationView.as_view(), name="create-restaurant"),
]
