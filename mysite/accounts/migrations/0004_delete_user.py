# Generated by Django 4.2.4 on 2023-08-10 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
