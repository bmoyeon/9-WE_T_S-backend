from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length = 100)
    menu = models.ForeignKey('Menu', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'categories'
