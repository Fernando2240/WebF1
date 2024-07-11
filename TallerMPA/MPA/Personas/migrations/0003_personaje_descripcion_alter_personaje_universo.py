# Generated by Django 4.1.5 on 2023-01-29 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Personas", "0002_remove_personaje_image_remove_universo_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="personaje",
            name="descripcion",
            field=models.CharField(default=True, max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="personaje",
            name="universo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Personas.universo"
            ),
        ),
    ]
