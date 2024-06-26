# Generated by Django 4.2.6 on 2023-11-03 19:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventId', models.AutoField(primary_key=True, serialize=False)),
                ('eventName', models.CharField(max_length=100)),
                ('hostName', models.CharField(max_length=50)),
                ('hostEmail', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('location', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('startTime', models.TimeField()),
                ('endDate', models.DateField(default=django.utils.timezone.now)),
                ('endTime', models.TimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('not started', 'NOT STARTED'), ('active', 'ACTIVE'), ('on going', 'ON GOING'), ('ended', 'ENDED')], default='not started', max_length=15)),
                ('invitees', models.TextField()),
                ('attendees', models.TextField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.category')),
            ],
        ),
    ]
