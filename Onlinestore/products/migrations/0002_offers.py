# Generated by Django 3.2.6 on 2021-08-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offrname', models.CharField(max_length=255)),
                ('offramt', models.FloatField()),
            ],
        ),
    ]