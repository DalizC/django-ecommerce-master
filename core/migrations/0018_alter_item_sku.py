# Generated by Django 4.2.2 on 2023-06-28 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_item_model_item_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sku',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
