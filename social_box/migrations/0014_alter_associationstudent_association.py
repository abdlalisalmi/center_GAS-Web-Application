# Generated by Django 3.2 on 2021-04-16 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_box', '0013_auto_20210416_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associationstudent',
            name='association',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_box.association'),
        ),
    ]
