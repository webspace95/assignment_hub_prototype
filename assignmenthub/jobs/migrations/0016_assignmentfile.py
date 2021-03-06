# Generated by Django 3.0.4 on 2022-01-19 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_auto_20220119_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=None)),
                ('date', models.DateTimeField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Order')),
            ],
        ),
    ]
