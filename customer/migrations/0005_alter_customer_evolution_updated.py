# Generated by Django 5.1 on 2024-08-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_customer_evolution_field_customer_evolution_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='evolution_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
