# Generated by Django 3.0.6 on 2020-05-19 19:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('temphum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=20, verbose_name='Codigo')),
                ('latidud', models.CharField(max_length=20, verbose_name='Latidud')),
                ('longitud', models.CharField(max_length=20, verbose_name='Longitud')),
                ('producto', models.CharField(max_length=25, verbose_name='Producto')),
                ('area', models.IntegerField(verbose_name='Area')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
