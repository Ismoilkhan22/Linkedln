from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


class CustomMG(UserManager):
    def create_user(self, username=None, password=None, email=None, is_staff=False, is_superuser=False,
                    **extra_fields):
        user = self.model(
            username=username,
            password=password,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields

        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return self.create_user(
            username=username,
            email=email,
            password=password,
            is_superuser=True,
            is_staff=True,
            **extra_fields

        )


class User(AbstractBaseUser, PermissionsMixin):
    fio = models.CharField(max_length=256)
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomMG()
    REQUIRED_FIELDS = ['username', 'password']
    USERNAME_FIELD = 'username'


class Profile(models.Model):
    fio = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    about = models.TextField()
    photo = models.ImageField(upload_to='imgs')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    imgs = models.ImageField(upload_to='posts')
    about = models.TextField()


class Jobs(models.Model):
    name = models.CharField(max_length=128)
    about = models.TextField()


class Chat(models.Model):
    pass


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
