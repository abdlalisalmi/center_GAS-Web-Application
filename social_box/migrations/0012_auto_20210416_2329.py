# Generated by Django 3.2 on 2021-04-16 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_box', '0011_association_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associationstudent',
            name='programm_Type',
        ),
        migrations.RemoveField(
            model_name='associationstudent',
            name='services',
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='A',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='B',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='C',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='ES',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='Ergo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='FP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='Ortho',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='Psy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='Psycom',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='Tronsport',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='associationstudent',
            name='keni',
            field=models.BooleanField(default=False),
        ),
    ]