# Generated by Django 3.1.1 on 2020-10-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitedtls',
            name='ConNum',
            field=models.IntegerField(blank=True, max_length=30, null=True),
        ),
    ]
