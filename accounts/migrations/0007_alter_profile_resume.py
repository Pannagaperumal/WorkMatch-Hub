# Generated by Django 5.1.2 on 2025-03-08 07:11

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auditlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/', validators=[accounts.models.validate_pdf]),
        ),
    ]
