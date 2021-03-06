# Generated by Django 3.0.4 on 2021-12-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20211216_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment_complete',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='academic_level',
            field=models.CharField(blank=True, choices=[('Hi', 'Highschool'), ('Co', 'College'), ('Un', 'University'), ('Ma', 'Masters'), ('Ph', 'PhD')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='days',
            field=models.CharField(blank=True, choices=[('1 ', '1 Hour'), ('2 ', '2 Hours'), ('3 ', '3 Hours'), ('6 ', '6 Hours'), ('12', '12 Hours'), ('24', '24 Hours'), ('2 ', '2 Days'), ('3 ', '3 Days'), ('4 ', '4 Days'), ('5 ', '5 Days'), ('6 ', '6 Days'), ('7 ', '7 Days'), ('15', '15 Days'), ('18', '18 Days'), ('20', '20 Days'), ('1 ', '1 Month')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='line_spacing',
            field=models.CharField(blank=True, choices=[('Si', 'Single Spacing (1.0)'), ('Do', 'Double Spacing (2.0)')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='number_of_pages',
            field=models.CharField(blank=True, choices=[('1 ', '1 Page'), ('2 ', '2 Pages'), ('3 ', '3 Pages'), ('4 ', '4 Pages'), ('5 ', '5 Pages'), ('6 ', '6 Pages'), ('7 ', '7 Pages'), ('8 ', '8 Pages'), ('9 ', '9 Pages'), ('10', '10 Pages'), ('11', '11 -  15 pages'), ('16', '16 - 20 pages'), ('21', '21 - 30 pages')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paper_format',
            field=models.CharField(blank=True, choices=[('ML', 'MLA'), ('AP', 'APA'), ('HA', 'HARVAD'), ('OX', 'OXFORD'), ('Ot', 'Other...')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='subject',
            field=models.CharField(blank=True, choices=[('Co', 'Computer science'), ('Me', 'Medical Sciences'), ('Ma', 'Management'), ('Ma', 'Maths'), ('St', 'Statistics'), ('En', 'Engineering')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(blank=True, choices=[('Ad', 'Admission Essay'), ('An', 'Analysis of any type'), ('Ar', 'Article/Book/Movie review'), ('Ca', 'Capstone Projects'), ('Co', 'Coursework'), ('Di', 'Dissertations'), ('La', 'Lab reports'), ('Pr', 'Presentations'), ('Re', 'Research papers and proposals'), ('Sp', 'Speaches'), ('Ex', 'Exams'), ('Ot', 'Other Subjects')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='files',
            field=models.ManyToManyField(blank=True, null=True, to='jobs.OrderFile'),
        ),
    ]
