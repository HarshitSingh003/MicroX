# Generated by Django 4.1.3 on 2022-11-23 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_apply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='Employer_Id',
            new_name='Employer_No',
        ),
        migrations.RenameField(
            model_name='apply',
            old_name='job_seeker_Id',
            new_name='job_seeker_No',
        ),
    ]