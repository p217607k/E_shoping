# Generated by Django 4.1.2 on 2022-10-18 17:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0006_alter_contect_us_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Ecommerce/Order')),
                ('quantity', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=10)),
                ('pincode', models.IntegerField(max_length=10)),
                ('datetime', models.DateField(default=datetime.date(2022, 10, 18))),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
