# Generated by Django 3.2.6 on 2021-08-29 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Student',
        ),
    ]
