# Generated by Django 2.1.5 on 2019-01-08 14:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideal_event', '0005_auto_20190108_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interest2',
            name='interest_level',
        ),
        migrations.AddField(
            model_name='interest',
            name='interest_level',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
