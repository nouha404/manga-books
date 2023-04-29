from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class UserManger(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Veillez entrer un email')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255, blank=False)
    pseudo = models.CharField(blank=True, max_length=8)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManger()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
