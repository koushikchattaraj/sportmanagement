# Generated by Django 3.2.9 on 2021-11-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturent', '0009_delete_uservalidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dpimage',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
