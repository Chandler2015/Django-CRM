# Generated by Django 2.2.5 on 2019-09-19 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0011_auto_20190919_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
