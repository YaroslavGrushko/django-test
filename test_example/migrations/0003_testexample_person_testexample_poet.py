# Generated by Django 5.0.1 on 2024-01-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_example', '0002_rename_firstname_testexample_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testexample',
            name='person',
            field=models.CharField(default='Hero', max_length=255),
        ),
        migrations.AddField(
            model_name='testexample',
            name='poet',
            field=models.CharField(default='poet', max_length=255),
        ),
    ]
