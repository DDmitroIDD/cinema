# Generated by Django 3.1.7 on 2021-03-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0006_auto_20210317_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieseance',
            name='show_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movieseance',
            name='show_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
