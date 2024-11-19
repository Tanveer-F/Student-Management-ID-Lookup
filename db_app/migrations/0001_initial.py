# Generated by Django 5.0.6 on 2024-11-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=40)),
                ('marks', models.IntegerField()),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
