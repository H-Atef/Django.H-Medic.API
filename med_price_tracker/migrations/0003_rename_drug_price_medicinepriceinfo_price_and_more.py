# Generated by Django 5.0.6 on 2024-12-04 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('med_price_tracker', '0002_medicinepriceinfo_search_q'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicinepriceinfo',
            old_name='drug_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='medicinepriceinfo',
            old_name='drug_repeat',
            new_name='repeat',
        ),
    ]
