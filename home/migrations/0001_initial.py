# Generated by Django 5.0.7 on 2024-10-06 03:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Masyli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('origin', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='masyli_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='SupernaturalAbilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='supernatural_photos/')),
                ('masyli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.masyli')),
            ],
        ),
    ]
