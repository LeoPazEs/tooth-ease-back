# Generated by Django 4.2.11 on 2024-05-15 01:37

import core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kids', '0004_alter_kid_birth_date_alter_kid_father_alter_kid_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kid',
            options={'verbose_name': 'Kid', 'verbose_name_plural': 'Kids'},
        ),
        migrations.AlterField(
            model_name='kid',
            name='birth_date',
            field=models.DateField(validators=[core.validators.future_date_validator], verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='kid',
            name='father',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kids', to=settings.AUTH_USER_MODEL, verbose_name='Father'),
        ),
        migrations.AlterField(
            model_name='kid',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]
