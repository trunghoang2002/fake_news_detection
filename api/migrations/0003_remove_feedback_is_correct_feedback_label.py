# Generated by Django 4.2.6 on 2023-12-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='is_correct',
        ),
        migrations.AddField(
            model_name='feedback',
            name='label',
            field=models.IntegerField(default=0),
        ),
    ]
