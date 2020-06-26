# Generated by Django 3.0.7 on 2020-06-26 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200625_1324'),
        ('product', '0002_auto_20200626_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.ProductSize'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.TypeName'),
        ),
        migrations.AlterField(
            model_name='productcolor',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Color'),
        ),
        migrations.AlterField(
            model_name='productcolor',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product'),
        ),
    ]
