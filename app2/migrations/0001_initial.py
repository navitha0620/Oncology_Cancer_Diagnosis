# Generated by Django 5.0.6 on 2024-06-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=10)),
                ('hospitalname', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=150)),
            ],
        ),
    ]
