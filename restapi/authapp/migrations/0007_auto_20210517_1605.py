# Generated by Django 3.2.2 on 2021-05-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210517_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='senha',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=0, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
