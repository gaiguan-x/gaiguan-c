# Generated by Django 2.2.6 on 2019-12-20 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20191219_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.BooleanField()),
                ('age', models.BooleanField()),
                ('sex', models.BooleanField()),
            ],
        ),
    ]
