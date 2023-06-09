# Generated by Django 4.1.7 on 2023-04-13 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0004_guest_host_remove_arrangements_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishments',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='establishments',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='date_create',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 4, 13, 20, 12, 54, 251116)),
        ),
    ]
