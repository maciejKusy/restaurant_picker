from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserRestaurantStack


class RestaurantStackInline(admin.StackedInline):
    model = UserRestaurantStack
    can_delete = False
    verbose_name_plural = 'userrestaurantstack'


class UserAdmin(BaseUserAdmin):
    inlines = (RestaurantStackInline,)


admin.site.register(User, UserAdmin)
admin.site.register(UserRestaurantStack)
