# Generated by Django 4.2.1 on 2023-05-18 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_transactiontype_expense_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='transaction_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tracker.transactiontype'),
        ),
    ]
