# Generated by Django 3.1.1 on 2020-11-07 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0014_testimonial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='Testimonial',
            new_name='testimonial',
        ),
    ]
