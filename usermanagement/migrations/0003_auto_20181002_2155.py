# Generated by Django 2.0.9 on 2018-10-02 19:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0002_auto_20181002_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 19, 55, 32, 639511, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='character',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 2, 19, 55, 32, 639538, tzinfo=utc)),
        ),
    ]
