# Generated by Django 5.0.3 on 2024-04-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0006_alter_consultation_details_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation_details',
            name='Diagnosis',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='consultation_details',
            name='symptoms',
            field=models.TextField(null=True),
        ),
    ]
