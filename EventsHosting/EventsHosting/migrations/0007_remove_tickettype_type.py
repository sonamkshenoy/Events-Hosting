# Generated by Django 2.2.4 on 2019-11-09 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventsHosting', '0006_tickettype_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickettype',
            name='type',
        ),
    ]
