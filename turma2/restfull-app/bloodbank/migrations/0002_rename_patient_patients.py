# Generated by Django 4.2.1 on 2023-05-23 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patient',
            new_name='Patients',
        ),
    ]
