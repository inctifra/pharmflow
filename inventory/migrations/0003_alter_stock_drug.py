# Generated by Django 5.2.3 on 2025-06-16 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_drug_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='drug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drug', to='inventory.drug'),
        ),
    ]
