# Generated by Django 4.2.4 on 2023-09-05 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_orderplaced_payment_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='mproduct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.milkproduct'),
        ),
    ]
