# Generated by Django 5.1.2 on 2025-03-23 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='antonyms',
        ),
        migrations.RemoveField(
            model_name='word',
            name='synonyms',
        ),
    ]
