# Generated by Django 2.2.5 on 2019-09-19 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0006_auto_20190919_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='where',
            new_name='where_to_hear',
        ),
    ]
