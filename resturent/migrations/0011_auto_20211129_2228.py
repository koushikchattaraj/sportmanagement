# Generated by Django 3.2.9 on 2021-11-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent', '0010_userprofile_dpimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
