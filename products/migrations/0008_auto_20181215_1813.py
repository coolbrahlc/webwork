# Generated by Django 2.1.4 on 2018-12-15 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181215_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='category',
        ),
    ]
