# Generated by Django 3.2.4 on 2021-06-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Savoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=50)),
                ('link_yt', models.CharField(max_length=200)),
                ('link_pdf', models.CharField(max_length=100)),
            ],
        ),
    ]
