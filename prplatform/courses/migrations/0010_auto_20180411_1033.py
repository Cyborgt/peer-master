# Generated by Django 2.0.4 on 2018-04-11 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0009_auto_20180411_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name of the course')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Course code')),
                ('url_slug', models.CharField(max_length=50, unique=True, verbose_name='Identifier that will be used in URL addressses')),
                ('school', models.CharField(max_length=20, verbose_name='Name abbreviation of the school, eg. TTY, UTA...')),
                ('teachers', models.ManyToManyField(related_name='teachers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='courseimplementation',
            name='course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='school',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teachers',
        ),
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(default=2017),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='url_slug',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.DeleteModel(
            name='CourseImplementation',
        ),
        migrations.AddField(
            model_name='course',
            name='base_course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.BaseCourse'),
            preserve_default=False,
        ),
    ]
