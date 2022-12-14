# Generated by Django 4.1.2 on 2022-10-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_remove_burner_photo_burner_photo_main_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                default=0, max_length=20, unique=False, verbose_name="URL"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="burner",
            name="photo_main",
            field=models.ImageField(upload_to="photos/", verbose_name="Фото 1"),
        ),
        migrations.AlterField(
            model_name="burner",
            name="photo_second",
            field=models.ImageField(
                blank=True, upload_to="photos/", verbose_name="Фото 2"
            ),
        ),
        migrations.AlterField(
            model_name="burner",
            name="photo_third",
            field=models.ImageField(
                blank=True, upload_to="photos/", verbose_name="Фото 3"
            ),
        ),
    ]
