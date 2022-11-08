# Generated by Django 2.0.4 on 2018-04-27 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0013_auto_20180426_0754'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name of the exercise')),
                ('description', models.CharField(blank=True, max_length=5000)),
                ('file_upload', models.BooleanField(default=False)),
                ('upload_instructions', models.CharField(blank=True, max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='courses.Course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]