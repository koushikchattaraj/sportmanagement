# Generated by Django 3.2.9 on 2021-12-09 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent', '0019_userprofile_follower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='reffer_by',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='refferal_code',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, choices=[('cricket', 'cricket'), ('football', 'user'), ('vollyball', 'volyball'), ('kabadi', 'kabadi')], max_length=20, null=True),
        ),
    ]
