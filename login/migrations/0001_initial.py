# Generated by Django 5.0.2 on 2024-03-03 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolename', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(default='', max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=200)),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.roles')),
            ],
        ),
    ]
