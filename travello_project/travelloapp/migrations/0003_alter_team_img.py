# Generated by Django 3.2.12 on 2022-03-14 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelloapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
