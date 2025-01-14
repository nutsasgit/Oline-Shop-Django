from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, identification_number, password, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            identification_number = identification_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, identification_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, identification_number, password, **extra_fields)

    def create_superuser(self, email, identification_number, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')

        return self._create_user(email, identification_number, password, **extra_fields)



class User (AbstractBaseUser, PermissionsMixin): #abstractuser qmnis avtomaturad password fields.
        email = models.EmailField(unique=True)
        identification_number = models.CharField(max_length=20, unique=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        is_vendor = models.BooleanField(default=False)
        is_customer = models.BooleanField(default=False)
        date_joined = models.DateTimeField(auto_now_add=True)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS =['identification_number']

        objects = AccountManager()