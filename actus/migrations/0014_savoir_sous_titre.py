# Generated by Django 3.2.4 on 2021-07-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actus', '0013_auto_20210705_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='savoir',
            name='sous_titre',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
