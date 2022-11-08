# Generated by Django 2.0.4 on 2018-04-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20180411_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.CharField(default='TTY', max_length=20, verbose_name='Name abbreviation of the school, eg. TTY, UTA...'),
            preserve_default=False,
        ),
    ]
