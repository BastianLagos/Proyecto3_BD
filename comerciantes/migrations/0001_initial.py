# Generated by Django 4.1 on 2022-11-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comerciante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.TextField(max_length=12)),
                ('razonsocial', models.TextField(max_length=100)),
                ('giro', models.TextField(max_length=100)),
                ('comuna', models.TextField(max_length=50)),
                ('direccion', models.TextField(max_length=100)),
                ('numeroventas', models.IntegerField()),
                ('estado', models.TextField(max_length=1)),
            ],
        ),
    ]
