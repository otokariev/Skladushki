from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    # slug = models.SlugField(max_length=255)  # !FIXME customize slug
    phone = models.CharField(max_length=255, blank=True, null=True)  # !FIXME Add phone check
    city = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)  # !FIXME Add parameters
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.user


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
