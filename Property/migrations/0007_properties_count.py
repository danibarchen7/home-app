# Generated by Django 4.2.11 on 2024-04-06 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0006_properties_ratestate_alter_properties_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
