# Generated by Django 2.1.4 on 2019-02-04 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0018_downloadtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewlock',
            name='group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.StudentGroup'),
        ),
    ]
