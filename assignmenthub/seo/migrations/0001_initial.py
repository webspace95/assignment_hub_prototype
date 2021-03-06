# Generated by Django 3.0.4 on 2021-12-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMetaField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutTitleField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DashboardMetaField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DashboardTitleField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IndexMetaField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IndexTitleField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderMetaField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderTitleField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrivacypolicyMetaField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PrivacypolicyTitleField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SampleMetaField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SampleTitleField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_description', models.CharField(max_length=100)),
            ],
        ),
    ]
