# Generated by Django 2.2.10 on 2021-05-17 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210515_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program_skill',
            name='depart_name_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dept_skill'),
        ),
        migrations.AlterField(
            model_name='program_skill',
            name='program_name_skill',
            field=models.CharField(max_length=100),
        ),
    ]
