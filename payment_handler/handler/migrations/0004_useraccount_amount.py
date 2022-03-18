# Generated by Django 4.0.3 on 2022-03-18 10:24

from django.db import migrations
import handler.models


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0003_useraccount_delete_useraccounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='amount',
            field=handler.models.PositiveDecimalField(decimal_places=4, default=0, max_digits=20),
        ),
    ]