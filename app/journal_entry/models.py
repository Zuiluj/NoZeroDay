from django.db import models

from user.models import User
# Create your models here.

class Journal(models.Model):
    name = models.CharField(verbose_name='name', max_length=22)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True)
    title = models.CharField(verbose_name='title', max_length=32, default='Title')
    date_created = models.DateField(auto_now_add=True)
    
    plan_today = models.TextField()
    did_today = models.TextField()
    plan_tom = models.TextField()

    def __str__(self):
        return self.title
