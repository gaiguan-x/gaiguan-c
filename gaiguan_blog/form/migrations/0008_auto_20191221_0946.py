# Generated by Django 2.2.6 on 2019-12-21 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20191220_1602'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Form',
        ),
        migrations.AddField(
            model_name='field',
            name='address',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='age',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='city',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='date',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='hobby',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='mail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='phone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='postal_code',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='school',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='sex',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='strong_point',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='text',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='field',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.BooleanField(default=False),
        ),
    ]
