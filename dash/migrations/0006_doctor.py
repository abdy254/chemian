# Generated by Django 3.1.1 on 2020-10-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0005_auto_20201029_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50, null=True)),
                ('doctor_details', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
