from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=255)  # name
    bio = models.TextField(blank=True)  # about
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class About(models.Model):
    header = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.header


class Contacts(models.Model):
    header = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.header
