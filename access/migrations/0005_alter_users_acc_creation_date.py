# Generated by Django 3.2.6 on 2021-10-12 15:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_alter_users_acc_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='acc_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 15, 46, 20, 323172, tzinfo=utc)),
        ),
    ]
