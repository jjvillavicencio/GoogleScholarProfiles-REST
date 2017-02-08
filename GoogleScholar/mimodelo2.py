# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AutorPublicacion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='CEDULA', max_length=11, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipo_docente = models.CharField(db_column='TIPO_DOCENTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_publicacion = models.CharField(db_column='TIPO_PUBLICACION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    abstract = models.TextField(db_column='ABSTRACT', blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='YEAR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    doi = models.CharField(db_column='DOI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='KEYWORDS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    enlace_articulo = models.CharField(db_column='ENLACE_ARTICULO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipo_documento = models.CharField(db_column='TIPO_DOCUMENTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estado_validacion = models.CharField(db_column='ESTADO_VALIDACION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scholar_url = models.TextField(db_column='SCHOLAR_URL', blank=True, null=True)  # Field name made lowercase.
    analizado = models.IntegerField(db_column='ANALIZADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_autor_publicacion'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class AutorPublicacion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='CEDULA', max_length=45, blank=True, null=True)  # Field name made lowercase.
    id_area = models.IntegerField(db_column='ID_AREA', blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_departamento = models.IntegerField(db_column='ID_DEPARTAMENTO', blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_seccion_departamental = models.IntegerField(db_column='ID_SECCION_DEPARTAMENTAL', blank=True, null=True)  # Field name made lowercase.
    seccion_departamental = models.CharField(db_column='SECCION_DEPARTAMENTAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo_docente = models.CharField(db_column='TIPO_DOCENTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo_publicacion = models.TextField(db_column='TIPO_PUBLICACION', blank=True, null=True)  # Field name made lowercase.
    id_articulo = models.IntegerField(db_column='ID_ARTICULO')  # Field name made lowercase.
    titulo = models.TextField(db_column='TITULO')  # Field name made lowercase.
    abstract = models.TextField(db_column='ABSTRACT')  # Field name made lowercase.
    id_area_conocimiento = models.IntegerField(db_column='ID_AREA_CONOCIMIENTO', blank=True, null=True)  # Field name made lowercase.
    area_conocimiento = models.CharField(db_column='AREA_CONOCIMIENTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_sub_area_conocimiento = models.IntegerField(db_column='ID_SUB_AREA_CONOCIMIENTO', blank=True, null=True)  # Field name made lowercase.
    sub_area_conocimiento = models.CharField(db_column='SUB_AREA_CONOCIMIENTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_area_conocimiento_especifica = models.IntegerField(db_column='ID_AREA_CONOCIMIENTO_ESPECIFICA', blank=True, null=True)  # Field name made lowercase.
    area_conocimiento_especifica = models.CharField(db_column='AREA_CONOCIMIENTO_ESPECIFICA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    id_indice = models.IntegerField(db_column='ID_INDICE', blank=True, null=True)  # Field name made lowercase.
    indice = models.TextField(db_column='INDICE', blank=True, null=True)  # Field name made lowercase.
    otro_indice = models.CharField(db_column='OTRO_INDICE', max_length=250)  # Field name made lowercase.
    doi = models.TextField(db_column='DOI')  # Field name made lowercase.
    revista = models.CharField(db_column='REVISTA', max_length=255)  # Field name made lowercase.
    keywords = models.TextField(db_column='KEYWORDS')  # Field name made lowercase.
    enlace_articulo = models.TextField(db_column='ENLACE_ARTICULO')  # Field name made lowercase.
    fecha_envio = models.DateField(db_column='FECHA_ENVIO', blank=True, null=True)  # Field name made lowercase.
    fecha_aceptacion = models.DateField(db_column='FECHA_ACEPTACION', blank=True, null=True)  # Field name made lowercase.
    fecha_publicacion = models.DateField(db_column='FECHA_PUBLICACION', blank=True, null=True)  # Field name made lowercase.
    autores = models.TextField(db_column='AUTORES', blank=True, null=True)  # Field name made lowercase.
    id_pais = models.IntegerField(db_column='ID_PAIS', blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='PAIS', max_length=765, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='CIUDAD', max_length=300)  # Field name made lowercase.
    quartil = models.IntegerField(db_column='QUARTIL', blank=True, null=True)  # Field name made lowercase.
    idioma = models.CharField(db_column='IDIOMA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    citas_scopus = models.IntegerField(db_column='CITAS_SCOPUS', blank=True, null=True)  # Field name made lowercase.
    citas_isi = models.IntegerField(db_column='CITAS_ISI', blank=True, null=True)  # Field name made lowercase.
    issn = models.CharField(db_column='ISSN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo_documento = models.CharField(db_column='TIPO_DOCUMENTO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombre_conferencia = models.CharField(db_column='NOMBRE_CONFERENCIA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=765, blank=True, null=True)  # Field name made lowercase.
    link_latindex = models.CharField(db_column='LINK_LATINDEX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    link_revista = models.CharField(db_column='LINK_REVISTA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sjr = models.DecimalField(db_column='SJR', max_digits=10, decimal_places=0)  # Field name made lowercase.
    volumne = models.IntegerField(db_column='VOLUMNE')  # Field name made lowercase.
    paginas = models.CharField(db_column='PAGINAS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issue = models.IntegerField(db_column='ISSUE')  # Field name made lowercase.
    afiliacion_utpl = models.CharField(db_column='AFILIACION_UTPL', max_length=5)  # Field name made lowercase.
    estado_validacion = models.CharField(db_column='ESTADO_VALIDACION', max_length=8)  # Field name made lowercase.
    analizado = models.IntegerField(db_column='ANALIZADO', blank=True, null=True)  # Field name made lowercase.
    scholar_url = models.TextField(db_column='SCHOLAR_URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'autor_publicacion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PerfilGoogle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='CEDULA', max_length=11)  # Field name made lowercase.
    scholar_id = models.TextField(db_column='SCHOLAR_ID')  # Field name made lowercase.
    coincidencia = models.IntegerField(db_column='COINCIDENCIA')  # Field name made lowercase.
    estado = models.IntegerField(db_column='ESTADO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfil_google'
