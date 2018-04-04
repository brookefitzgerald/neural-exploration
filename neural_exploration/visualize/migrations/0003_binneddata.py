# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-22 17:44
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0002_load_zhang_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinnedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_150_50', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=10, max_digits=15), blank=True, null=True, size=None), blank=True, null=True, size=None)),
                ('bin_100_30', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=10, max_digits=15), blank=True, null=True, size=None), blank=True, null=True, size=None)),
                ('bin_50_15', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=10, max_digits=15), blank=True, null=True, size=None), blank=True, null=True, size=None)),
                ('bin_150_50_extents', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None), blank=True, null=True, size=None)),
                ('bin_100_30_extents', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None), blank=True, null=True, size=None)),
                ('bin_50_15_extents', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None), blank=True, null=True, size=None)),
                ('labels', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, null=True), blank=True, null=True, size=None)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualize.Site')),
            ],
        ),
    ]
