# Generated by Django 5.1.7 on 2025-03-23 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('company', models.CharField(max_length=300)),
                ('status', models.CharField(choices=[('A', 'Active'), ('UA', 'Un Active')], default='A', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(default='')),
                ('activity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.activity_type')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.employee')),
            ],
        ),
    ]
