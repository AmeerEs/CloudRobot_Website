# Generated by Django 3.1.5 on 2021-05-31 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='measurement',
        ),
    ]
