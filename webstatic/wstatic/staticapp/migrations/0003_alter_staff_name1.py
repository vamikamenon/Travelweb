# Generated by Django 4.2.1 on 2023-08-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0002_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='name1',
            field=models.CharField(max_length=250),
        ),
    ]
