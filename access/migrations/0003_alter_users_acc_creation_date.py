# Generated by Django 3.2.6 on 2021-10-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_alter_users_acc_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='acc_creation_date',
            field=models.DateTimeField(),
        ),
    ]
