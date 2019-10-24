from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(verbose_name='name', max_length=50)
    email = models.EmailField(verbose_name='email', max_length=54, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)

    is_active = models.BooleanField(default=True)

        
    def __str__(self):
        return self.name

    def get_name(self):
        return self.name