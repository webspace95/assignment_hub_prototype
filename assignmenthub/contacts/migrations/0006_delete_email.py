# Generated by Django 3.0.4 on 2021-12-01 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20211128_1318'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email',
        ),
    ]