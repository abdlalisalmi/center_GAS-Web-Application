# Generated by Django 3.2 on 2021-04-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handicapped', '0006_auto_20210410_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='handicapped',
            name='has_card',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='request_card',
            field=models.BooleanField(default=False),
        ),
    ]
