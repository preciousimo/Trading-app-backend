# Generated by Django 4.1.7 on 2023-03-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradingaccount',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
