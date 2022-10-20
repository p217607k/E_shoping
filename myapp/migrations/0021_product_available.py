# Generated by Django 4.1.2 on 2022-10-19 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.CharField(choices=[('In stack', 'In stack'), ('Out of stack', 'Out of stack')], max_length=100, null='True'),
            preserve_default='True',
        ),
    ]
