# Generated by Django 3.2.4 on 2021-06-29 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actus', '0004_savoir_disponible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savoir',
            name='numero',
        ),
        migrations.AddField(
            model_name='savoir',
            name='ouvert_par_defaut',
            field=models.CharField(default='', max_length=10),
        ),
    ]
