# Generated by Django 2.1.5 on 2019-01-08 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideal_event', '0008_auto_20190108_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='interests',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideal_event.KeyVal'),
        ),
    ]
