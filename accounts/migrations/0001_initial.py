# Generated by Django 2.0.7 on 2018-08-06 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('CID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('domain', models.CharField(default='', max_length=20)),
                ('package', models.IntegerField(default=50000)),
                ('pointer', models.FloatField(default=6.5)),
                ('arrivaldate', models.DateField()),
                ('eligible', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=25)),
                ('city', models.CharField(default='', max_length=20)),
                ('branch', models.CharField(default='', max_length=20)),
                ('year', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='12345six', max_length=15)),
                ('s1', models.FloatField(default=0)),
                ('s2', models.FloatField(default=0)),
                ('s3', models.FloatField(default=0)),
                ('s4', models.FloatField(default=0)),
                ('s5', models.FloatField(default=0)),
                ('s6', models.FloatField(default=0)),
                ('s7', models.FloatField(default=0)),
                ('s8', models.FloatField(default=0)),
                ('cgpa', models.FloatField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
