# Generated by Django 4.1 on 2022-08-31 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0002_photo_slug_alter_photo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
