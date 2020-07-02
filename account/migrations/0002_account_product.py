# Generated by Django 3.0.7 on 2020-06-30 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0003_auto_20200626_0904'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='product',
            field=models.ManyToManyField(through='order.CartWishlist', to='product.Product'),
        ),
    ]