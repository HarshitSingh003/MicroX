# Generated by Django 4.1.3 on 2022-11-22 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_token',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
