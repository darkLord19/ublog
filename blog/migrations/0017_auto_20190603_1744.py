# Generated by Django 2.1.7 on 2019-06-03 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190603_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 3, 12, 14, 48, 108036, tzinfo=utc)),
        ),
    ]