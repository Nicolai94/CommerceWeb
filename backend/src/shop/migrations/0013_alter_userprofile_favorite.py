# Generated by Django 4.1.1 on 2022-09-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_userprofile_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorite',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorite_product', to='shop.product', verbose_name='Избранное'),
        ),
    ]
