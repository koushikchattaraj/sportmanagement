# Generated by Django 3.2.9 on 2021-12-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent', '0014_auto_20211201_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
