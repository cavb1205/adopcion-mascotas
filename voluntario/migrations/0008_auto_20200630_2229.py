# Generated by Django 3.0.7 on 2020-06-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluntario', '0007_auto_20200630_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades_voluntario',
            name='extra',
            field=models.TextField(blank=True, verbose_name='Sugerencia'),
        ),
    ]