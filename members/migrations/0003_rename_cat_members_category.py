# Generated by Django 4.2.8 on 2023-12-12 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_women_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='cat',
            new_name='category',
        ),
    ]