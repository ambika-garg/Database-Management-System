# Generated by Django 2.2.10 on 2021-05-14 09:04

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant_entre',
            name='mobile_entre_mobile_number',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=66, size=6),
        ),
        migrations.AlterField(
            model_name='participant_skill',
            name='mobile_skill_mobile_number',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=66, size=6),
        ),
    ]