# Generated by Django 5.1.2 on 2024-10-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_jobpost_budget_jobpost_job_duration_jobpost_job_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('full_time', 'Full-Time'), ('part_time', 'Part-Time'), ('freelance', 'Freelance'), ('contract', 'Contract'), ('temporary', 'Temporary'), ('one_time', 'One-Time Task')], default='contract', max_length=50),
        ),
    ]
