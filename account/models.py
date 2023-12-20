from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models


class Account(AbstractUser):
    account_pk = models.AutoField(primary_key=True)

    def __str__(self):
        return self.account_pk

    # groups = models.ManyToManyField(Group, related_name="account_groups")
    # account_permissions = models.ManyToManyField(Permission, related_name="account_permissions_set",)

    # def save(self, **kwargs):
    #     super().save(**kwargs)
    #     if not self.password:
    #         return
    #     self.set_password(self.password)
    #


class AccountProfile(models.Model):
    # slug = models.SlugField(max_length=255)  # !FIXME customize slug
    phone = models.CharField(max_length=255, blank=True, null=True)  # !FIXME Add phone check
    city = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)  # !FIXME Add parameters
    sex = models.ForeignKey('Sex', verbose_name='Пол', on_delete=models.PROTECT)
    account = models.OneToOneField('Account', verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.account


class Sex(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class Contacts(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.title
