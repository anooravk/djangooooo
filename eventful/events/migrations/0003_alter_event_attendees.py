# Generated by Django 4.2.6 on 2023-11-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.TextField(default=''),
        ),
    ]
