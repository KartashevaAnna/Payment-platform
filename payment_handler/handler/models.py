from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserAccounts(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
