# Generated by Django 3.0.7 on 2020-06-28 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_color_button_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='button_url',
            new_name='button_color',
        ),
    ]
