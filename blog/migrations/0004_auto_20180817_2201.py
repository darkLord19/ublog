# Generated by Django 2.0.7 on 2018-08-17 16:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180803_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='random', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 17, 16, 30, 47, 619371, tzinfo=utc)),
        ),
    ]
