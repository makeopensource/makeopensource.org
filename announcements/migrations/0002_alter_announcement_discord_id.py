# Generated by Django 3.2.3 on 2021-06-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='discord_id',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
    ]
