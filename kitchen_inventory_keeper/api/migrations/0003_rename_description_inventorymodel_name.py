# Generated by Django 5.0.3 on 2024-04-18 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_inventoryitemsmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventorymodel',
            old_name='description',
            new_name='name',
        ),
    ]
