# Generated by Django 2.1.7 on 2019-04-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0015_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'Menu',
            },
        ),
    ]
