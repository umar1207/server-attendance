# Generated by Django 4.1.7 on 2023-08-17 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2023, 8, 17, 11, 53, 19, 845326)),
        ),
        migrations.AlterField(
            model_name='log',
            name='time_in',
            field=models.TimeField(verbose_name=datetime.datetime(2023, 8, 17, 11, 53, 19, 845339)),
        ),
    ]
