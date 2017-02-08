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
        db_table = 'autor_publicacion'

    def __unicode__(self):
        return "%s %s" % (self.apellido, self.nombre)


class PerfilGoogle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='CEDULA', max_length=11)  # Field name made lowercase.
    scholar_id = models.TextField(db_column='SCHOLAR_ID')  # Field name made lowercase.
    coincidencia = models.IntegerField(db_column='COINCIDENCIA')  # Field name made lowercase.
    estado = models.IntegerField(db_column='ESTADO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfil_google'

    def __unicode__(self):
        return "%s" % (self.cedula)
