# Generated by Django 2.2.12 on 2020-06-24 21:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activitymanager', '0002_auto_20200624_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='start_time',
            field=models.DateTimeField(db_column='start_time', default=django.utils.timezone.now),
        ),
    ]
