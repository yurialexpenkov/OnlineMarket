from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
# from app_shops.models import History


class Profile(models.Model):
    STATUS_CHOICES = [
        ('active_user', 'active user'),
        ('inactive user', 'inactive user'),
          ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    status = models.CharField(max_length=30, null=True, default='inactive user', choices=STATUS_CHOICES,)
    balance = models.FloatField(verbose_name='баланс', default=0)

    class Meta:
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')

