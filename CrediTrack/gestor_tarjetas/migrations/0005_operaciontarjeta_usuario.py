# Generated by Django 5.0.1 on 2024-01-28 23:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_tarjetas', '0004_alter_operaciontarjeta_cantidad_cuotas'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='operaciontarjeta',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operaciones', to=settings.AUTH_USER_MODEL),
        ),
    ]
