# Generated by Django 2.2.10 on 2020-04-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0019_auto_20200401_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]