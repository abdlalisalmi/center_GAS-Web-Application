# Generated by Django 3.2 on 2021-04-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_box', '0006_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
