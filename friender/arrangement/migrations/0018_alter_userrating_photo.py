# Generated by Django 4.1.7 on 2023-05-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0017_alter_establishmentsrating_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo_ratings'),
        ),
    ]
