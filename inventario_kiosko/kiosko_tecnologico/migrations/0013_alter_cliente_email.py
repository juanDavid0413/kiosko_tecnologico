# Generated by Django 5.1 on 2024-09-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosko_tecnologico', '0012_factura_productos_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
