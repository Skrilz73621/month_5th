# Generated by Django 5.1.5 on 2025-02-08 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_remove_movie_review_review_movie_alter_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='review',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='movie_app.review'),
        ),
    ]
