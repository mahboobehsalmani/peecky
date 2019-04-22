# Generated by Django 2.1.7 on 2019-04-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_owns_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('value', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'BusinessInfo',
            },
        ),
    ]
