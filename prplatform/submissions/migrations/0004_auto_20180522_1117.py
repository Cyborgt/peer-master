# Generated by Django 2.0.4 on 2018-05-22 11:17

from django.db import migrations, models
import prplatform.submissions.models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_auto_20180517_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originalsubmission',
            name='file',
            field=models.FileField(blank=True, upload_to=prplatform.submissions.models.upload_fp),
        ),
    ]