# Generated by Django 3.2.4 on 2021-06-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savoir',
            name='numero',
            field=models.CharField(default='0', max_length=3),
        ),
    ]
