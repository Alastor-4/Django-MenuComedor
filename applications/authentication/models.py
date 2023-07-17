from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


# Modelo para la creación de usuarios
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Usuario", max_length=15, unique=True)
    email = models.EmailField("Correo", unique=True)
    codregistro = models.CharField("Codigo", max_length=6, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = [
        "email",
    ]

    objects = UserManager()

    def __str__(self):
        return self.username
