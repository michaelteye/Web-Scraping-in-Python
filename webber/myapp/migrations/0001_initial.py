# Generated by Django 3.2.9 on 2021-11-20 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
