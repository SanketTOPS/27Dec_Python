# Generated by Django 5.1.7 on 2025-04-10 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('pphoto', models.ImageField(upload_to='Products')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.products')),
            ],
        ),
    ]
