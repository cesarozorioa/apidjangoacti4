# Generated by Django 5.0.6 on 2024-06-13 00:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appservidor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librodb',
            name='autor_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autores', to='appservidor.autordb'),
        ),
    ]
