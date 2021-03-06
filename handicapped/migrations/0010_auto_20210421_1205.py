# Generated by Django 3.2 on 2021-04-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handicapped', '0009_handicapped_association'),
    ]

    operations = [
        migrations.RenameField(
            model_name='handicapped',
            old_name='has_card',
            new_name='B',
        ),
        migrations.RenameField(
            model_name='handicapped',
            old_name='request_card',
            new_name='C',
        ),
        migrations.AddField(
            model_name='handicapped',
            name='A',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='ES',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='Ergo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='FP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='Ortho',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='Psy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='Psycom',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='Tronsport',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='deleted_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='handicapped',
            name='keni',
            field=models.BooleanField(default=False),
        ),
    ]
