# Generated by Django 3.2.6 on 2021-10-12 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0003_alter_users_acc_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='acc_creation_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 21, 14, 49, 343790)),
        ),
    ]