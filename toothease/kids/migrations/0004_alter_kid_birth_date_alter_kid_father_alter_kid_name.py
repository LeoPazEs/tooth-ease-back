# Generated by Django 4.2.11 on 2024-04-14 14:15

import core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kids', '0003_alter_kid_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='birth_date',
            field=models.DateField(validators=[core.validators.future_date_validator], verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='kid',
            name='father',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kids', to=settings.AUTH_USER_MODEL, verbose_name='Pai'),
        ),
        migrations.AlterField(
            model_name='kid',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
    ]