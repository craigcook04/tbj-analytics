# Generated by Django 3.0.dev20190822120949 on 2019-08-28 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jays_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='division',
        ),
        migrations.RemoveField(
            model_name='team',
            name='venue',
        ),
        migrations.AddField(
            model_name='team',
            name='link',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='teamId',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
