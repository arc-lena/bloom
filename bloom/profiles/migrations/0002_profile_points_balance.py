# Generated by Django 4.2 on 2024-10-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='points_balance',
            field=models.IntegerField(default=0),
        ),
    ]