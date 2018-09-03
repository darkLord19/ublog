# Generated by Django 2.0.7 on 2018-09-01 13:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180817_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('technology', 'Technology'), ('personal', 'Personal'), ('poetry', 'Poetry'), ('rants', 'Rants'), ('random', 'Random')], default='technology', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 13, 28, 29, 266064, tzinfo=utc)),
        ),
    ]
