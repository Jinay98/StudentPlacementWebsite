# Generated by Django 2.0.7 on 2018-08-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='UID',
            field=models.IntegerField(default=0, null=True),
        ),
    ]