# Generated by Django 3.2.12 on 2022-03-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelloapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics1')),
                ('dec', models.TextField()),
            ],
        ),
    ]
