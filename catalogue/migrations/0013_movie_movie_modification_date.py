# Generated by Django 5.0.7 on 2024-07-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_movie_movie_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_modification_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación registro de película'),
        ),
    ]
