# Generated by Django 3.2.4 on 2021-07-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRUEBAFINAL', '0023_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.IntegerField(choices=[(0, 'Categoria'), (2, 'Comestibles'), (1, 'Bebidas'), (3, 'Varios')], default=0),
        ),
    ]
