# Generated by Django 3.0.4 on 2021-12-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_delete_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whatsapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
            ],
        ),
    ]