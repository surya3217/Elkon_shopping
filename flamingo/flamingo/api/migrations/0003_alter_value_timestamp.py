# Generated by Django 3.2.11 on 2022-03-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_date_created_value_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
