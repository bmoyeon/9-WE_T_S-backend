from django.db import models

class Product(models.Model):
    name         = models.CharField(max_length = 50)
    price        = models.DecimalField(max_digits = 20, decimal_places = 4)
    guide        = models.CharField(max_length = 500, blank = True)
    category     = models.ForeignKey('menu.Category', on_delete = models.SET_NULL, null = True)
    size         = models.ManyToManyField('Size', through = 'ProductSize')
    color        = models.ManyToManyField('Color', through = 'ProductColor')
    created_at   = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'products'

class Size(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'sizes'

class ProductSize(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    size    = models.ForeignKey('Size', on_delete = models.CASCADE)

    class Meta:
        db_table = 'product_sizes'

class Color(models.Model):
    name  = models.CharField(max_length = 50)
    image = models.URLField(max_length = 2000)

    class Meta:
        db_table = 'colors'

class ProductColor(models.Model):
    color   = models.ForeignKey('Color', on_delete = models.CASCADE)
    product = models.ForeignKey('Product', on_delete = models.CASCADE)

    class Meta:
        db_table = 'product_colors'

class Image(models.Model):
    image_url    = models.URLField(max_length = 2000)
    is_thumbnail = models.BooleanField(default = False)
    color        = models.ForeignKey('ProductColor', on_delete = models.CASCADE)

    class Meta:
        db_table = 'images'
