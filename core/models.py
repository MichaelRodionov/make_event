from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from core.managers import UserManager


# ----------------------------------------------------------------
# user model
class User(AbstractBaseUser):
    """
    Model representing a user

    Attrs:
        - email: User email
        - organization: user's organization
        - is_staff: defines permissions to admin panel
        - USERNAME_FIELD: redefines username to email
        - objects: define UserManager
    """
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    organization = models.ForeignKey(
        'organizations.Organization',
        on_delete=models.PROTECT,
        verbose_name='Организация',
        null=True,
        related_name='users'
    )
    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD: str = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label) -> bool:
        return True

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'
