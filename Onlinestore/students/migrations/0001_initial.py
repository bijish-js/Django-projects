# Generated by Django 3.2.6 on 2021-08-29 14:17

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('mark1', models.IntegerField()),
                ('mark2', models.IntegerField()),
                ('mark3', models.IntegerField()),
            ],
            managers=[
                ('Objects', django.db.models.manager.Manager()),
            ],
        ),
    ]