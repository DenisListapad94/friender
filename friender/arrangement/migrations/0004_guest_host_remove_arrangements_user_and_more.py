# Generated by Django 4.1.7 on 2023-04-13 16:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0003_alter_passport_date_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='arrangement.users')),
                ('min_bill_value', models.PositiveIntegerField(null=True)),
            ],
            bases=('arrangement.users',),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('users_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='arrangement.users')),
                ('max_spend_value', models.PositiveIntegerField(null=True)),
            ],
            bases=('arrangement.users',),
        ),
        migrations.RemoveField(
            model_name='arrangements',
            name='user',
        ),
        migrations.AlterField(
            model_name='passport',
            name='date_create',
            field=models.DateTimeField(auto_created=datetime.datetime(2023, 4, 13, 19, 49, 34, 651681)),
        ),
        migrations.AddField(
            model_name='arrangements',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='arrangement.guest'),
        ),
        migrations.AddField(
            model_name='arrangements',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='arrangement.host'),
        ),
    ]
