# Generated by Django 2.2.6 on 2019-12-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0012_auto_20191221_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=50, verbose_name='省份')),
                ('city', models.CharField(max_length=50, verbose_name='城市')),
                ('district', models.CharField(max_length=50, verbose_name='区域')),
            ],
            options={
                'verbose_name_plural': '城市数据表',
            },
        ),
    ]
