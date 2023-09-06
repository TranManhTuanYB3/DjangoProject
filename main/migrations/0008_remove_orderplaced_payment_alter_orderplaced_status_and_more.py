# Generated by Django 4.2.4 on 2023-09-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_payment_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment',
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Đã xác nhận', 'Đã xác nhận'), ('Đóng gói', 'Đóng gói'), ('Đang vận chuyển', 'Đang vận chuyển'), ('Đã giao', 'Đã giao'), ('Huỷ đơn', 'Huỷ đơn'), ('Chờ xác nhận', 'Chờ xác nhận')], default='Chờ xác nhận', max_length=50),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]