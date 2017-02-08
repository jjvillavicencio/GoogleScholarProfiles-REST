# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutorPublicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=11, null=True, db_column=b'CEDULA', blank=True)),
                ('email', models.CharField(max_length=50, null=True, db_column=b'EMAIL', blank=True)),
                ('tipo_docente', models.CharField(max_length=100, null=True, db_column=b'TIPO_DOCENTE', blank=True)),
                ('apellido', models.CharField(max_length=100, null=True, db_column=b'APELLIDO', blank=True)),
                ('nombre', models.CharField(max_length=100, null=True, db_column=b'NOMBRE', blank=True)),
                ('tipo_publicacion', models.CharField(max_length=100, null=True, db_column=b'TIPO_PUBLICACION', blank=True)),
                ('titulo', models.CharField(max_length=500, null=True, db_column=b'TITULO', blank=True)),
                ('abstract', models.TextField(null=True, db_column=b'ABSTRACT', blank=True)),
                ('year', models.CharField(max_length=100, null=True, db_column=b'YEAR', blank=True)),
                ('doi', models.CharField(max_length=100, null=True, db_column=b'DOI', blank=True)),
                ('keywords', models.CharField(max_length=500, null=True, db_column=b'KEYWORDS', blank=True)),
                ('enlace_articulo', models.CharField(max_length=200, null=True, db_column=b'ENLACE_ARTICULO', blank=True)),
                ('tipo_documento', models.CharField(max_length=200, null=True, db_column=b'TIPO_DOCUMENTO', blank=True)),
                ('estado', models.CharField(max_length=200, null=True, db_column=b'ESTADO', blank=True)),
                ('estado_validacion', models.CharField(max_length=100, null=True, db_column=b'ESTADO_VALIDACION', blank=True)),
                ('scholar_url', models.TextField(null=True, db_column=b'SCHOLAR_URL', blank=True)),
                ('analizado', models.IntegerField(null=True, db_column=b'ANALIZADO', blank=True)),
            ],
            options={
                'db_table': 'autor_publicacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerfilGoogle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=11, db_column=b'CEDULA')),
                ('scholar_id', models.TextField(db_column=b'SCHOLAR_ID')),
                ('coincidencia', models.IntegerField(db_column=b'COINCIDENCIA')),
                ('estado', models.FloatField(db_column=b'ESTADO')),
            ],
            options={
                'db_table': 'perfil_google',
                'managed': False,
            },
        ),
    ]
