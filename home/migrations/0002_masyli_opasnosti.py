# Generated by Django 5.0.7 on 2024-10-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='masyli',
            name='opasnosti',
            field=models.CharField(choices=[('K', 'kolosalni'), ('O', 'opasni'), ('N', 'neizvestni'), ('NN', 'neitral'), ('B', 'bezopasni')], default='O', max_length=2),
        ),
    ]
