# Generated by Django 4.1.5 on 2023-01-15 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_alter_movie_director"),
    ]

    operations = [
        migrations.AddField(
            model_name="director",
            name="biographic",
            field=models.TextField(blank=True, null=True, verbose_name="Resumen"),
        ),
    ]