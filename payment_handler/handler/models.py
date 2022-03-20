from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import DecimalField
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


User = get_user_model()

CURRENCY_CHOICES = (
    ('RUBLE', 'ruble'),
    ('DOLLAR', 'dollar'),
    ('EURO', 'euro'),
)


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _("%(value)s is not positive."),
            params={"value": value}
        )


class PositiveDecimalField(DecimalField):
    description = _("Positive decimal number")

    @cached_property
    def validators(self):
        return super().validators + [validate_positive]


class UserAccount(models.Model):
    amount = PositiveDecimalField(decimal_places=4, max_digits=20, default=0)
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


class Transationtion(models.Model):
    amount = PositiveDecimalField(decimal_places=4, max_digits=20, default=0)
    date = models.DateTimeField(auto_now_add=True)
