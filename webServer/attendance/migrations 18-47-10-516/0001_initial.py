# Generated by Django 4.1.7 on 2023-08-04 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('team', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateField(verbose_name=datetime.datetime(2023, 8, 4, 12, 54, 27, 967876))),
                ('time_in', models.TimeField(verbose_name=datetime.datetime(2023, 8, 4, 12, 54, 27, 967888))),
                ('time_out', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('team', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]