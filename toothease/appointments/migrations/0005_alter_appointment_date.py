# Generated by Django 4.2.11 on 2024-05-27 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_alter_appointment_date_alter_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(verbose_name='Date'),
        ),
    ]
