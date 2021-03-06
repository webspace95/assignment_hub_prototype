# Generated by Django 3.0.4 on 2021-12-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20211216_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='academic_level',
            field=models.CharField(blank=True, choices=[('H', 'Highschool'), ('C', 'College'), ('U', 'University'), ('M', 'Masters'), ('P', 'PhD')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='days',
            field=models.CharField(blank=True, choices=[('1', '1 Hour'), ('2', '2 Hours'), ('3', '3 Hours'), ('6', '6 Hours'), ('1', '12 Hours'), ('2', '24 Hours'), ('2', '2 Days'), ('3', '3 Days'), ('4', '4 Days'), ('5', '5 Days'), ('6', '6 Days'), ('7', '7 Days'), ('1', '15 Days'), ('1', '18 Days'), ('2', '20 Days'), ('1', '1 Month')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='line_spacing',
            field=models.CharField(blank=True, choices=[('S', 'Single Spacing (1.0)'), ('D', 'Double Spacing (2.0)')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='number_of_pages',
            field=models.CharField(blank=True, choices=[('1', '1 Page'), ('2', '2 Pages'), ('3', '3 Pages'), ('4', '4 Pages'), ('5', '5 Pages'), ('6', '6 Pages'), ('7', '7 Pages'), ('8', '8 Pages'), ('9', '9 Pages'), ('1', '10 Pages'), ('1', '11 -  15 pages'), ('1', '16 - 20 pages'), ('2', '21 - 30 pages')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paper_format',
            field=models.CharField(blank=True, choices=[('M', 'MLA'), ('A', 'APA'), ('H', 'HARVAD'), ('O', 'OXFORD'), ('O', 'Other...')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='subject',
            field=models.CharField(blank=True, choices=[('C', 'Computer science'), ('M', 'Medical Sciences'), ('M', 'Management'), ('M', 'Maths'), ('S', 'Statistics'), ('E', 'Engineering')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(blank=True, choices=[('A', 'Admission Essay'), ('A', 'Analysis of any type'), ('A', 'Article/Book/Movie review'), ('C', 'Capstone Projects'), ('C', 'Coursework'), ('D', 'Dissertations'), ('L', 'Lab reports'), ('P', 'Presentations'), ('R', 'Research papers and proposals'), ('S', 'Speaches'), ('E', 'Exams'), ('O', 'Other Subjects')], max_length=2, null=True),
        ),
    ]
