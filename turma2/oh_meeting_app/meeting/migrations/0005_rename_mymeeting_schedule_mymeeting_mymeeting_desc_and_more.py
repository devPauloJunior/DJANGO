# Generated by Django 4.2.1 on 2023-06-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_alter_mymeeting_mymeeting_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymeeting',
            old_name='mymeeting_schedule',
            new_name='mymeeting_desc',
        ),
        migrations.AlterField(
            model_name='mymeeting',
            name='mymeeting_link',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='mymeeting',
            name='mymeeting_room',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
