# Generated by Django 2.2.12 on 2020-06-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200623_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_column='email', max_length=254, unique=True),
        ),
    ]
