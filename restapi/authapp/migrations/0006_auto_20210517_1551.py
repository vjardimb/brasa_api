# Generated by Django 3.2.2 on 2021-05-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='senha',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
