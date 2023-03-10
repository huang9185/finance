# Generated by Django 4.0.5 on 2023-03-03 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystocks', '0004_alter_watch_first_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('quote', models.CharField(max_length=10)),
                ('first_created', models.DateTimeField(auto_now_add=True)),
                ('number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('quote', models.CharField(max_length=10)),
                ('first_created', models.DateTimeField(auto_now_add=True)),
                ('number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('quote', models.CharField(max_length=10)),
                ('numberTotal', models.IntegerField()),
                ('paidTotal', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
