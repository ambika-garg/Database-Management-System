# Generated by Django 2.2.10 on 2021-05-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210518_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant_entre',
            name='mobile_entre_primary_mobile',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='participant_entre',
            name='mobile_entre_secondary_mobile',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='participant_skill',
            name='mobile_skill_primary_mobile',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='participant_skill',
            name='mobile_skill_secondary_mobile',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
