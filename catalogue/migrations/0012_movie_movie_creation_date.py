# Generated by Django 5.0.7 on 2024-07-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_movie_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creacion registro de película'),
        ),
    ]
