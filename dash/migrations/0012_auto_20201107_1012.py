# Generated by Django 3.1.1 on 2020-11-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0011_online_appointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
