# Generated by Django 3.2.4 on 2021-07-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRUEBAFINAL', '0026_auto_20210707_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='codigo',
            field=models.CharField(max_length=2),
        ),
    ]
