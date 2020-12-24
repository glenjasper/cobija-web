# Generated by Django 2.2.17 on 2020-12-24 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='Description', verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'Pet color',
                'verbose_name_plural': 'Pet color',
                'db_table': 'cobija_petcolor',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PetSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='Description', verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'Pet size',
                'verbose_name_plural': 'Pet size',
                'db_table': 'cobija_petsize',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TypePartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='Description', verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'Type of partner',
                'verbose_name_plural': 'Types of partner',
                'db_table': 'cobija_typepartner',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TypePet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(blank=True, help_text='Description', verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'Type of pet',
                'verbose_name_plural': 'Types of pet',
                'db_table': 'cobija_typepet',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
