# Generated by Django 4.0.3 on 2022-04-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_form_edits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academiclevel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='day',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='format',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spacing',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='type',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
