# Generated by Django 3.2 on 2021-04-10 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handicapped', '0004_auto_20210410_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='handicapped',
            old_name='Genre',
            new_name='genre',
        ),
    ]
