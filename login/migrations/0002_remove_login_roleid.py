# Generated by Django 5.0.2 on 2024-03-05 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='roleid',
        ),
    ]
