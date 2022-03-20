# Generated by Django 4.0.3 on 2022-03-20 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0002_alter_restaurant_name"),
        ("users", "0003_userrestaurantpick_delete_userrestaurantstack"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userrestaurantpick",
            name="restaurant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="picks",
                to="restaurants.restaurant",
            ),
        ),
    ]
