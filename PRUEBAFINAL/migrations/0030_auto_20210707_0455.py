# Generated by Django 3.2.4 on 2021-07-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRUEBAFINAL', '0029_auto_20210707_0454'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.IntegerField(choices=[(3, 'Varios'), (1, 'Bebidas'), (0, 'Categoria'), (2, 'Comestibles')], default=0),
        ),
    ]
