# Generated by Django 3.2.16 on 2022-12-31 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Requester', '0005_applied_rides'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel_info',
            old_name='transport_request',
            new_name='applied_transport_request',
        ),
    ]
