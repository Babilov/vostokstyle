# Generated by Django 4.1.2 on 2022-10-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_remove_burner_photo_main_remove_burner_photo_second_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="heater",
            name="pressure",
            field=models.FloatField(default=0, verbose_name="Мощность"),
            preserve_default=False,
        ),
    ]
