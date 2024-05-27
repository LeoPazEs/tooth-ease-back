# Generated by Django 4.2.11 on 2024-04-14 14:15

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, validators=[core.validators.future_date_validator], verbose_name='Birth Date'),
        ),
    ]
