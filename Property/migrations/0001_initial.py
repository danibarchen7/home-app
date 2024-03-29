# Generated by Django 4.2.8 on 2023-12-26 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('area', models.FloatField()),
                ('site', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('n_bathroom', models.IntegerField()),
                ('n_room', models.IntegerField()),
                ('type_r', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=50)),
                ('n_bed', models.IntegerField()),
                ('n_salon', models.IntegerField()),
                ('furntiure', models.BooleanField(default=True)),
                ('wifi', models.BooleanField(default=True)),
                ('garden', models.BooleanField(default=True)),
                ('pool', models.BooleanField(default=True)),
                ('elevator', models.BooleanField(default=True)),
                ('soloar_system', models.BooleanField(default=True)),
                ('idt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Type.tipe')),
            ],
        ),
    ]
