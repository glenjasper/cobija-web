# Generated by Django 2.2.17 on 2020-12-24 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='adopted',
            field=models.BooleanField(default=False, verbose_name='Adopted'),
        ),
    ]