from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class UserModel(AbstractUser):
    user_pk = models.AutoField(primary_key=True)
    # password_2 = models.CharField(max_length=128, null=True, blank=True)  #!FIXME check
    groups = models.ManyToManyField(Group, related_name="user_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="user_user_permissions")

    def save(self, **kwargs):
        super().save(**kwargs)
        if not self.password:
            return
        self.set_password(self.password)
        # if not self.password:
        #     return
        # if self.password_2 != self.password:
        #     raise ValidationError({"password_2": ["Пароли должны совпадать."]})  #!FIXME check

    def __str__(self):
        return self.user_pk


# @receiver(pre_save, sender=UserModel)  #!FIXME check
# def check_passwords(sender, instance, **kwargs):
#     if instance.password_1 != instance.password_2:
#         raise ValidationError("Пароли не совпадают")


class UserProfile(models.Model):
    # slug = models.SlugField(max_length=255)  # !FIXME customize slug
    phone = models.CharField(max_length=255, blank=True, null=True)  # !FIXME Add phone check
    city = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)  # !FIXME Add parameters
    sex = models.ForeignKey('Sex', on_delete=models.PROTECT)
    user_model = models.ForeignKey(UserModel, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_model


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
