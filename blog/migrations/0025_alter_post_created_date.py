# Generated by Django 4.1.3 on 2022-11-20 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20200912_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 20, 12, 16, 16, 784862, tzinfo=datetime.timezone.utc)),
        ),
    ]