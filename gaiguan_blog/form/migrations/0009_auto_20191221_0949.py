# Generated by Django 2.2.6 on 2019-12-21 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_auto_20191221_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='is_used',
            field=models.BooleanField(default=True),
        ),
    ]
