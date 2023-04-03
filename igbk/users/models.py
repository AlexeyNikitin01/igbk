from django.db import models
from django.contrib.auth.models import User


class ProfileUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

