# Generated by Django 3.2.11 on 2022-03-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_value_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='value',
            field=models.IntegerField(),
        ),
    ]
