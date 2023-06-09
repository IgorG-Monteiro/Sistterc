# Generated by Django 4.0.5 on 2023-02-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terceirizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('unidade', models.CharField(max_length=100)),
                ('contrato', models.CharField(max_length=100)),
                ('vigencia', models.DateField()),
                ('contratada', models.CharField(max_length=100)),
                ('cnpj_contratada', models.CharField(max_length=18)),
                ('usuario_cadastro', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
