# Generated by Django 3.2 on 2021-07-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210712_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='password',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Пароль от машины'),
        ),
        migrations.AlterField(
            model_name='car',
            name='password_confirm',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Подтверждение пароля от машины'),
        ),
    ]
