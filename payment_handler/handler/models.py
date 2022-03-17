from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


User = get_user_model()

CURRENCY_CHOICES = (
    ('RUBLE', 'ruble'),
    ('DOLLAR', 'dollar'),
    ('EURO', 'euro'),
)


class UserAccount(models.Model):
    amount = models.DecimalField(decimal_places=4, max_digits=20),
    currency = models.CharField(
        max_length=6,
        choices=CURRENCY_CHOICES,
        default='RUBLE'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='accounts',
    )
