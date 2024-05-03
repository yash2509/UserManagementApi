from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from UserManagement.manager import CustomUserManager


class user(AbstractBaseUser):
    mob=models.CharField(null=True,unique=True)
    username=models.CharField(max_length=50,unique=True)
    is_superuser= None
    last_login = None
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.username

