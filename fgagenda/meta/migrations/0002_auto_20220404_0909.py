# Generated by Django 3.2.6 on 2022-04-04 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meta',
            name='todolist',
        ),
        migrations.AlterField(
            model_name='meta',
            name='dataInicio',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
