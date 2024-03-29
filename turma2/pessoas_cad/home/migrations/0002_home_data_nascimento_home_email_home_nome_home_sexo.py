# Generated by Django 4.1.7 on 2023-03-14 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='data_nascimento',
            field=models.DateField(default='2000-10-10', verbose_name='Data de Nascimento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='email',
            field=models.EmailField(default=' ', max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='nome',
            field=models.CharField(default=' ', max_length=100, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('I', 'Indefindo'), ('N', 'Nenhuma das opções')], default=' ', max_length=1, verbose_name='Sexo'),
            preserve_default=False,
        ),
    ]
