# Generated by Django 4.2.9 on 2024-01-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
