# Generated by Django 2.2 on 2022-10-31 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('total_price', models.IntegerField()),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
    ]