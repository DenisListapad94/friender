# Generated by Django 4.1.7 on 2023-04-13 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0006_alter_passport_date_create_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='date_create',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 4, 13, 21, 43, 21, 44195)),
        ),
    ]
