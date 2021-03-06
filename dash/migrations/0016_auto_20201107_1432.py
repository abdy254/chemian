# Generated by Django 3.1.1 on 2020-11-07 14:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0015_auto_20201107_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='online_appointments',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='online_appointments',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
