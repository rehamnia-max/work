# Generated by Django 4.1.5 on 2023-01-22 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('work_app', '0002_worker_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
