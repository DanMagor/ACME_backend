# Generated by Django 2.1.2 on 2018-11-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_auto_20181113_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acmeuser',
            name='avatar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='acmeuser',
            name='token',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
