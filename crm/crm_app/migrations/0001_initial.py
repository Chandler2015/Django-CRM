# Generated by Django 2.2.5 on 2019-09-19 17:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=200)),
                ('industry', models.CharField(choices=[('OIL/GAS', 'Oil/Gas'), ('FARMING', 'farming'), ('CONSTRUCTION', 'construction')], default='OIL/GAS', max_length=2)),
                ('follow_up_date', models.DateField(blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 9, 19, 17, 41, 29, 39194, tzinfo=utc))),
            ],
        ),
    ]
