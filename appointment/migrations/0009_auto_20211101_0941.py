# Generated by Django 3.2.7 on 2021-11-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0008_alter_appointment_accepted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='edit',
            field=models.BooleanField(default=False),
        ),
    ]