from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from customers.models import Office


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name='activo')
    date_joined = models.DateTimeField(default=timezone.now)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, blank=True, verbose_name='oficina')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'cuenta'
        verbose_name_plural = 'cuentas'
        ordering = ['-date_joined']

    def __str__(self):
        return self.email
