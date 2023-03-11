from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
        name = models.CharField("Имя", max_length=20)
        last_name = models.CharField('Фамилия', max_length=20)
        email = models.EmailField("Email", unique=True)
        age = models.IntegerField('Возраст', max_length=3)
        avatar = models.ImageField("Фото", upload_to="user_images/", null=True, blank=True)
        created = models.DateTimeField("Дата создания", auto_now_add=True)
        phone = models.CharField(
            'Номер телефона',
            null=True,
            max_length=10,
            unique = True
        )
        USERNAME_FIELD = 'phone'
        REQUIRED_FIELDS = []

        objects = UserManager()

class Doctor(AbstractUser):
    name = models.CharField("Имя", max_length=20)
    last_name = models.CharField('Фамилия', max_length=20)
    email = models.EmailField("Email", unique=True)
    avatar = models.ImageField("Фото", upload_to="user_images/", null=True, blank=True)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    special_key = models.CharField('Ключ регистрации', max_length=200)
    phone = models.CharField(
        'Номер телефона',
        null=True,
        max_length=10,
        unique=True
    )
    is_superuser = True
    is_active = True

    objects = UserManager()