# Generated by Django 2.0.7 on 2018-08-17 17:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [('blog', '0007_auto_20180817_2253')]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(
                default=datetime.datetime(2018, 8, 17, 17, 24, 7, 896653, tzinfo=utc)
            ),
        )
    ]
