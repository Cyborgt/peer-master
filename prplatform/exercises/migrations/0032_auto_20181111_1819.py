# Generated by Django 2.1.2 on 2018-11-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0031_reviewexercise_minimum_reviews_per_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewexercise',
            name='type',
            field=models.CharField(choices=[('RANDOM', 'Random by other user (prefer oldest with least peer-reviews)'), ('CHOOSE', 'Student chooses')], default='RANDOM', max_length=10),
        ),
    ]