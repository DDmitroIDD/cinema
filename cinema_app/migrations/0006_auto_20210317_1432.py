# Generated by Django 3.1.7 on 2021-03-17 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0005_auto_20210316_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movieseance',
            options={'ordering': ['is_active', 'show_start_date', 'start_time_seance']},
        ),
    ]
