# Generated by Django 2.1.2 on 2018-11-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20181015_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='temporary',
            field=models.BooleanField(default=False),
        ),
    ]