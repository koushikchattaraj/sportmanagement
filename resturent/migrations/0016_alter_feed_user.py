# Generated by Django 3.2.9 on 2021-12-01 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resturent', '0015_auto_20211201_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturent.userprofile'),
        ),
    ]
