# Generated by Django 5.0.6 on 2024-06-22 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_register_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='hospitalname',
            new_name='Hospitalname',
        ),
    ]
