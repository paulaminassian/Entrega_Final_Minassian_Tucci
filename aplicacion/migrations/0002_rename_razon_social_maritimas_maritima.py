# Generated by Django 5.0.1 on 2024-02-06 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maritimas',
            old_name='razon_social',
            new_name='maritima',
        ),
    ]
