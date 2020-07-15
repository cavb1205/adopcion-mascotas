# Generated by Django 3.0.7 on 2020-07-15 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0005_maltrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veterinarias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='images/veterinarias/')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefonos', models.CharField(max_length=255)),
                ('horarios', models.CharField(max_length=255)),
            ],
        ),
    ]
