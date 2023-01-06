# Generated by Django 3.1.5 on 2021-07-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_auto_20210702_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='session',
        ),
        migrations.RemoveField(
            model_name='agenttask',
            name='session',
        ),
        migrations.RemoveField(
            model_name='snapshot',
            name='session',
        ),
        migrations.RemoveField(
            model_name='task',
            name='session',
        ),
        migrations.AddField(
            model_name='report',
            name='describtion',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='agenttask',
            name='comment',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.DeleteModel(
            name='session',
        ),
    ]
