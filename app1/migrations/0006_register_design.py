# Generated by Django 5.0.6 on 2024-06-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_hospitalname_register_hospitalname'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='design',
            field=models.CharField(default='user', max_length=15),
        ),
    ]
