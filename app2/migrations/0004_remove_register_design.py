# Generated by Django 5.0.6 on 2024-08-28 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_register_design'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='design',
        ),
    ]
