# Generated by Django 4.1.1 on 2022-09-15 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_userprofile_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя пользователя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Купленный товар',
                'verbose_name_plural': 'Купленные товары',
                'ordering': ('created',),
            },
        ),
    ]
