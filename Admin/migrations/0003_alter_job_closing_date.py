# Generated by Django 5.0 on 2023-12-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_company_job_delete_adminlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='closing_date',
            field=models.DateField(),
        ),
    ]
