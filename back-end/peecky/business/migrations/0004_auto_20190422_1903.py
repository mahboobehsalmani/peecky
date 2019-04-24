# Generated by Django 2.1.7 on 2019-04-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20190422_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='latitude',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='longitude',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='website',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
