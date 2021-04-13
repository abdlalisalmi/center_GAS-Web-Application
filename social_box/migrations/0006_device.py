# Generated by Django 3.2 on 2021-04-13 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handicapped', '0007_auto_20210410_1418'),
        ('social_box', '0005_alter_project_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(blank=True, max_length=100, null=True)),
                ('device_name', models.TextField(blank=True, null=True)),
                ('submiting_date', models.DateField(auto_now_add=True)),
                ('approving_date', models.DateField(blank=True, null=True)),
                ('is_finish', models.BooleanField(default=False)),
                ('handicapped', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='handicapped.handicapped')),
            ],
        ),
    ]
