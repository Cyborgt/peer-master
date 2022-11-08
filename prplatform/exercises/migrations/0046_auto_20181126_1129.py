# Generated by Django 2.1.2 on 2018-11-26 11:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0045_reviewexercise_show_reviews_only_to_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=2), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='reviewexercise',
            name='can_review_own_submission',
            field=models.BooleanField(default=False, verbose_name='Students can peer-review themselves'),
        ),
    ]
