# Generated by Django 2.0.4 on 2018-04-10 11:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]