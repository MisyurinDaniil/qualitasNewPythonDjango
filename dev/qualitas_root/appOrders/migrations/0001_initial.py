# Generated by Django 4.0.5 on 2023-02-07 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appProductItem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_product_url', models.CharField(max_length=255, verbose_name='URL товара')),
                ('order_date', models.DateTimeField(auto_now=True, verbose_name='Дата заказа')),
                ('order_customer_name', models.CharField(max_length=255, verbose_name='Имя заказчика')),
                ('order_customer_telephone', models.CharField(max_length=255, verbose_name='Телефон заказчика')),
                ('order_customer_comment', models.TextField(verbose_name='Комментарий к заказу')),
                ('order_binding', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appProductItem.productitem', verbose_name='Ссылка на покупаемый товар')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
