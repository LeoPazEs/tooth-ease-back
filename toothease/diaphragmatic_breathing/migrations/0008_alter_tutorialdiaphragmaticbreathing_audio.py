# Generated by Django 4.2.11 on 2024-06-03 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaphragmatic_breathing', '0007_delete_audiotutorialdiaphragmaticbreathing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialdiaphragmaticbreathing',
            name='audio',
            field=models.FileField(upload_to='audioTutorialDiaphragmaticBreathing/', verbose_name='Audio'),
        ),
    ]
