# Generated by Django 3.2 on 2021-04-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_box', '0002_auto_20210413_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='approving_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
