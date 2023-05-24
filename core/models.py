from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# ----------------------------------------------------------------
# user model
class User(AbstractBaseUser):
    email: str = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'
