# Generated by Django 3.0.2 on 2020-04-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoportal', '0005_auto_20200428_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='path',
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=30),
        ),
    ]
