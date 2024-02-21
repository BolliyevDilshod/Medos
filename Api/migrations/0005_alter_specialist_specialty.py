# Generated by Django 5.0.2 on 2024-02-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_alter_hospitals_type_alter_pharmacys_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='specialty',
            field=models.CharField(blank=True, choices=[('lor', 'Lor'), ('jarroh', 'Jarroh'), ('urolog', 'Urolog'), ('genekolog', 'Genekolog'), ('akusher', 'Akusher')], max_length=100, null=True),
        ),
    ]