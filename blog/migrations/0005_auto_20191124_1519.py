# Generated by Django 2.2.6 on 2019-11-24 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191113_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alzheimer',
            name='idade',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
        migrations.CreateModel(
            name='Segmentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca1_right', models.DecimalField(decimal_places=6, max_digits=10)),
                ('ca1_left', models.DecimalField(decimal_places=6, max_digits=10)),
                ('ca2_ca3_right', models.DecimalField(decimal_places=6, max_digits=10)),
                ('ca2_ca3_left', models.DecimalField(decimal_places=6, max_digits=10)),
                ('subic_right', models.DecimalField(decimal_places=6, max_digits=10)),
                ('subic_left', models.DecimalField(decimal_places=6, max_digits=10)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Alzheimer')),
            ],
        ),
    ]
