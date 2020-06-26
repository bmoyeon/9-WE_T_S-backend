from django.db import models

from menu.models import TypeName


class ProductSize(models.Model):
    size      = models.CharField(max_length=10)

    class Meta:
        db_table = 'product_sizes'

class Product(models.Model):
    name         = models.CharField(max_length=50)
    price        = models.DecimalField(max_digits=20, decimal_places=4)
    created_at   = models.DateTimeField(auto_now_add=True)
    guide        = models.CharField(max_length=500, null=True)
    product_size = models.ForeignKey('ProductSize', on_delete=models.CASCADE)
    type_name    = models.ForeignKey('TypeName', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Color(models.Model):
    name    = models.CharField(max_length=100)
    product = models.ManyToManyField('Product', through = 'ProductColor')

    class Meta:
        db_table = 'colors'

class ProductColor(models.Model):
    color   = models.ForeignKey('Colors', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_colors'

class ProductImage(models.Model):
    image         = models.CharField(max_length=400)
    product_color = models.ForeignKey('ProductColor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'
