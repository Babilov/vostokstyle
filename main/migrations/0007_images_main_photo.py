# Generated by Django 4.1.2 on 2022-10-31 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_burner_item_alter_heater_item_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="images",
            name="main_photo",
            field=models.BooleanField(default=False),
        ),
    ]
