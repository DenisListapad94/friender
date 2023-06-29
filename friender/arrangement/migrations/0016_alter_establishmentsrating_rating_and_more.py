# Generated by Django 4.1.7 on 2023-05-16 18:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0015_userrating_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishmentsrating',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator, django.core.validators.MinValueValidator]),
        ),
        migrations.AlterField(
            model_name='userrating',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator, django.core.validators.MinValueValidator]),
        ),
    ]
