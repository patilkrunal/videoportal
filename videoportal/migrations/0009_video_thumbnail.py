# Generated by Django 3.0.2 on 2020-04-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoportal', '0008_auto_20200428_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.FileField(default='1.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]
