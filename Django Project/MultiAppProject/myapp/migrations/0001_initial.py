# Generated by Django 5.1.7 on 2025-04-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('mobile', models.BigIntegerField()),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
