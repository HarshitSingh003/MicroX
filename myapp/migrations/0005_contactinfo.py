# Generated by Django 4.1.3 on 2022-11-25 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_apply_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('msg', models.TextField(max_length=100)),
            ],
        ),
    ]