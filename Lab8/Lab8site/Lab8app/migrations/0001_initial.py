# Generated by Django 3.1.4 on 2020-12-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
    ]