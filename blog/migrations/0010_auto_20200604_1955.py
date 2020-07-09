# Generated by Django 3.0.5 on 2020-06-04 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200604_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alzheimer',
            name='folder',
        ),
        migrations.RemoveField(
            model_name='alzheimer',
            name='resultado',
        ),
        migrations.AddField(
            model_name='alzheimer',
            name='resultado_ad',
            field=models.DecimalField(decimal_places=2, default='00.0', max_digits=6),
        ),
        migrations.AddField(
            model_name='alzheimer',
            name='resultado_cn',
            field=models.DecimalField(decimal_places=2, default='00.0', max_digits=6),
        ),
    ]
