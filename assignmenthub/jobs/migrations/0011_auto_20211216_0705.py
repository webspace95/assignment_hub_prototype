# Generated by Django 3.0.4 on 2021-12-16 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20211213_1236'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcademicLevel',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Format',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='Spacing',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
