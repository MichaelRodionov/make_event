from django.contrib.auth.models import BaseUserManager


# ----------------------------------------------------------------
# user manager
class UserManager(BaseUserManager):
    """
    Class representing a user manager
    """
    def create_user(self, email, password=None):
        """
        Redefined method to create user
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """
        Redefined method to create superuser
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)
