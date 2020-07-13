# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('herbname', models.CharField(max_length=200)),
                ('image', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('xiangsidu', models.FloatField(null=True)),
                ('cass', models.CharField(max_length=200)),
                ('pubchem', models.CharField(max_length=200)),
                ('inchikey', models.CharField(max_length=200)),
                ('druglikeness', models.CharField(max_length=200)),
                ('category', models.ForeignKey(related_name='products', to='shop.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
