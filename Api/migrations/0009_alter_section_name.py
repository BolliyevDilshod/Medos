# Generated by Django 5.0.2 on 2024-02-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0008_alter_specialist_specialty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(choices=[('Terapiya', 'Terapiya'), ('Lor', 'Lor'), ('Reanimatsiya', 'Reanimatsiya'), ('Tramatologiya', 'Tramatologiya'), ('Hirurgiya', 'Hirurgiya'), ('Genekologiya', 'Genekologiya'), ('Urologiya', 'Urologiya'), ('uqumli_kasalliklar', 'Yuqumli Kasalliklar')], max_length=100, null=True),
        ),
    ]
