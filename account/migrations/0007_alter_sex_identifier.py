# Generated by Django 4.2.8 on 2024-01-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_sex_identifier_alter_sex_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sex',
            name='identifier',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]