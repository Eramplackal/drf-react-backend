# Generated by Django 5.1.2 on 2024-10-28 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todo_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completed',
        ),
    ]
