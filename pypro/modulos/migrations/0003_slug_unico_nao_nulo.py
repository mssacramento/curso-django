# Generated by Django 4.0.3 on 2022-03-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_modulo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
