# Generated by Django 3.2.6 on 2021-10-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0006_alter_users_acc_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
