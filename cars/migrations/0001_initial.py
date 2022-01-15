# Generated by Django 4.0.1 on 2022-01-14 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=256, verbose_name='Registration number')),
                ('max_pax', models.CharField(max_length=256, verbose_name='Maximum number of passengers')),
                ('make_year', models.IntegerField(verbose_name='Year of manufacture')),
                ('manufacturer', models.CharField(max_length=256, verbose_name='Car manufacturer')),
                ('model', models.CharField(max_length=256, verbose_name='Car model')),
                ('category', models.CharField(choices=[('EN', 'ECONOMY'), ('BN', 'BUSINESS'), ('FC', 'FIRST CLASS')], max_length=256, verbose_name='Car category')),
                ('engine', models.CharField(choices=[('EV', 'ELECTRIC'), ('HY', 'HYBRID'), ('IC', 'INTERNAL COMBUSTION ENGINE')], max_length=256, verbose_name='Engine type')),
                ('car_type', models.CharField(max_length=256, verbose_name='Car Type')),
            ],
        ),
    ]
