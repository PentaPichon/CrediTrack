# Generated by Django 5.0.1 on 2024-01-28 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_tarjetas', '0003_calendario_delete_cuota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operaciontarjeta',
            name='cantidad_cuotas',
            field=models.PositiveIntegerField(choices=[(1, '1'), (3, '3'), (6, '6'), (9, '9'), (12, '12')], default=1),
        ),
    ]
