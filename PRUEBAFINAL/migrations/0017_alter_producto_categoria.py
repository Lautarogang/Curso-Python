# Generated by Django 3.2.4 on 2021-07-01 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRUEBAFINAL', '0016_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.IntegerField(choices=[(3, 'Varios'), (0, 'Categoria'), (1, 'Bebidas'), (2, 'Comestibles')], default=0),
        ),
    ]
