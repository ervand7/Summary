# Generated by Django 3.2 on 2021-07-14 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_car_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='email',
            new_name='username',
        ),
    ]
