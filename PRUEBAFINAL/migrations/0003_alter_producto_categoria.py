# Generated by Django 3.2.4 on 2021-06-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRUEBAFINAL', '0002_auto_20210617_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.IntegerField(choices=[(3, 'Varios'), (0, 'Categoria'), (2, 'Comestibles'), (1, 'Bebidas')], default=0),
        ),
    ]