# Generated by Django 3.1.7 on 2021-03-13 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qnt', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='movieseance',
            name='end_time_seance',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movieseance',
            name='show_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movieseance',
            name='show_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='cinema_app.cinemahall'),
        ),
        migrations.AlterField(
            model_name='movieseance',
            name='show_start_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='movieseance',
            name='start_time_seance',
            field=models.TimeField(blank=True),
        ),
        migrations.DeleteModel(
            name='Buy',
        ),
        migrations.AddField(
            model_name='buying',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.movieseance'),
        ),
        migrations.AddField(
            model_name='buying',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL),
        ),
    ]
