# Generated by Django 5.0.7 on 2024-07-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_remove_movie_description_remove_movie_director_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='movies', verbose_name='Imagen'),
        ),
    ]