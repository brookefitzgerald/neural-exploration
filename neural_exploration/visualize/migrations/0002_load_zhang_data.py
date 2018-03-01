# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-15 16:04
from __future__ import unicode_literals
import environ
import numpy as np
from os import listdir
from scipy.io import loadmat

from django.db import migrations


def col_to_str_row(array):
    return str(np.round([item[0] for item in array], 5))


def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Experiment = apps.get_model("visualize", "Experiment")
    zhang_experiment = Experiment(
        slug="zhang",
        name="Zhang-Desimone 7 Object Spike Data",
        index_stimulus_shown=501,
        description="The Zhang-Desimone 7 Object dataset was collected by\
        Ying Zhang in Bob Desimone's lab at the McGovern Institute at MIT\
        itute at MIT. The data consists of single unit recordings from 13\
        2 neurons in the inferior temporal cortex (IT). Seven objects wer\
        e shown to the monkey in one of three locations, and were present\
        ed approxmately 20 times at each location.",
    )
    Experiment.objects.using(db_alias).bulk_create([zhang_experiment])
    Site = apps.get_model("visualize", "Site")
    Metadata = apps.get_model("visualize", "Metadata")
    zhang_data_directory = str(environ.Path().path('neural_exploration',
                                                   'visualize',
                                                   'migrations',
                                                   'zhang_data'))

    map_get_zero = np.vectorize(lambda x: x[0])
    for i, mat_file in enumerate(listdir(zhang_data_directory)):
        if i % 10 == 0:
            print('Reading site number: ' + str(i))
        mat_data = loadmat(zhang_data_directory + '/' + mat_file)
        data = mat_data['raster_data'].tolist()
        labels_one = map_get_zero(mat_data['raster_labels'][0][0][0][0]).tolist()
        labels_two = map_get_zero(mat_data['raster_labels'][0][0][1][0]).tolist()
        labels_three = map_get_zero(mat_data['raster_labels'][0][0][2][0]).tolist()
        metadata_variables = mat_data['raster_site_info'][0].dtype.names
        metadata_values = [
            np.ndarray.flatten(val)[0] if len(
                val) == 1 else col_to_str_row(val)
            for val in mat_data['raster_site_info'][0][0]
        ]

        metadata = zip(metadata_variables, metadata_values)

        site_slug = mat_file[2:6] + '_' + mat_file[10:12]
        zhang_site = Site(
            slug=site_slug,
            experiment=zhang_experiment,
            labels_one=labels_one,
            labels_two=labels_two,
            labels_three=labels_three,
            data = data)
        Site.objects.using(db_alias).bulk_create([zhang_site])

        Metadata.objects.using(db_alias).bulk_create([
            Metadata(
                site=zhang_site,
                information_variable=var,
                information_value=val) for (var, val) in metadata
        ])


class Migration(migrations.Migration):

    dependencies = [
        ('visualize', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
