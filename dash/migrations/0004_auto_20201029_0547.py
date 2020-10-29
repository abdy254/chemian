# Generated by Django 3.1.1 on 2020-10-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_auto_20201029_0531'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=500, null=True)),
                ('about_body', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='title',
            name='about_body',
        ),
        migrations.RemoveField(
            model_name='title',
            name='about_title',
        ),
    ]