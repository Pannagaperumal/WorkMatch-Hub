# Generated by Django 5.1.2 on 2024-12-16 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_application'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobalert',
            old_name='industry',
            new_name='job_description',
        ),
    ]
