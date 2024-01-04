# Generated by Django 4.2.1 on 2023-06-30 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bloodbank', '0003_patients_patient_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appointments_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('appointments_title', models.CharField(max_length=60)),
                ('appointments_desc', models.CharField(max_length=150)),
                ('appointments_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbank.patients')),
            ],
        ),
    ]
