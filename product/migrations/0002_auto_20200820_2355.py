# Generated by Django 3.1 on 2020-08-20 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='size',
            old_name='size',
            new_name='name',
        ),
    ]
