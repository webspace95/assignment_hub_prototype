# Generated by Django 3.0.4 on 2022-02-10 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_edits', '0008_auto_20211216_0714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='howweworktext',
            old_name='body',
            new_name='introduction',
        ),
    ]
