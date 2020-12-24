# Generated by Django 2.2.17 on 2020-12-24 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='facebook',
            field=models.URLField(blank=True, max_length=150, verbose_name='Facebook link'),
        ),
        migrations.AddField(
            model_name='member',
            name='instagram',
            field=models.URLField(blank=True, max_length=150, verbose_name='Instagram link'),
        ),
    ]