# Generated by Django 3.1.1 on 2020-11-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0016_auto_20201107_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='online_appointments',
            name='date',
        ),
        migrations.RemoveField(
            model_name='online_appointments',
            name='time',
        ),
        migrations.AlterField(
            model_name='p_appointment',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='p_appointment',
            name='time',
            field=models.TimeField(),
        ),
    ]
