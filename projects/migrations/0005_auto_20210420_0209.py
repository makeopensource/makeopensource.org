# Generated by Django 3.1.7 on 2021-04-20 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210420_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='release_date',
            field=models.DateField(),
        ),
    ]
