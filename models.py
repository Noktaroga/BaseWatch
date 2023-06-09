# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddressVTRDb(models.Model):
    
    iden_vivienda_gis = models.IntegerField(db_column='IDEN_VIVIENDA_GIS', blank=True, null=True)  # Field name made lowercase.
    mac_cm = models.TextField(db_column='MAC_CM', blank=True, null=True)  # Field name made lowercase.
    nom_direc = models.TextField(db_column='NOM_DIREC', blank=True, null=True)  # Field name made lowercase.
    cod_loca = models.TextField(db_column='COD_LOCA', blank=True, null=True)  # Field name made lowercase.
    cod_nodo = models.IntegerField(db_column='COD_NODO', blank=True, null=True)  # Field name made lowercase.
    cod_cuadrante = models.IntegerField(db_column='COD_CUADRANTE', blank=True, null=True)  # Field name made lowercase.
    num_latit = models.FloatField(db_column='NUM_LATIT', blank=True, null=True)  # Field name made lowercase.
    num_longit = models.FloatField(db_column='NUM_LONGIT', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True,db_column='ID_DJANGO',blank=False,null=False)

    class Meta:
        managed = False
        db_table = 'AddressVTRDb'


class CapacidadesAppProfile(models.Model):
    image = models.CharField(max_length=100)
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Capacidades_App_profile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Capacidad(models.Model):
    ano_solicitud = models.CharField(db_column='Ano_Solicitud', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sgi_indice = models.CharField(db_column='ID_SGI', unique=True, max_length=500, blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(db_column='Zona', max_length=500, blank=True, null=True)  # Field name made lowercase.
    asignacion_energφa = models.CharField(db_column='Asignacion_Energφa', max_length=500)  # Field name made lowercase.
    cantidad_n = models.CharField(db_column='Cantidad_N', max_length=500)  # Field name made lowercase.
    clase_zona_roja = models.CharField(db_column='Clase_Zona_Roja', max_length=500)  # Field name made lowercase.
    clave = models.CharField(db_column='Clave', max_length=500)  # Field name made lowercase.
    clientes_afectados = models.CharField(db_column='Clientes_Afectados', max_length=500)  # Field name made lowercase.
    comuna = models.CharField(db_column='Comuna', max_length=500, blank=True, null=True)  # Field name made lowercase.
    cuadrantes = models.CharField(db_column='Cuadrantes', max_length=500)  # Field name made lowercase.
    eps = models.CharField(db_column='EPS', max_length=500)  # Field name made lowercase.
    estado_asignacion_energφa = models.CharField(db_column='Estado_Asignaci≤n_Energφa', max_length=500)  # Field name made lowercase.
    estado_capo = models.CharField(db_column='Estado_CaPO', max_length=500)  # Field name made lowercase.
    estado_design_simplificado = models.CharField(db_column='Estado_Design_Simplificado', max_length=500)  # Field name made lowercase.
    estado_ejecucion = models.CharField(db_column='Estado_Ejecucion', max_length=500)  # Field name made lowercase.
    estado_ejecucion_2 = models.CharField(db_column='Estado_Ejecucion_2', max_length=500)  # Field name made lowercase.
    fecha_cancelado = models.CharField(db_column='Fecha_Cancelado', max_length=500)  # Field name made lowercase.
    fecha_comunicacion_eps = models.CharField(db_column='Fecha_Comunicacion_EPS', max_length=500)  # Field name made lowercase.
    fecha_design = models.CharField(db_column='Fecha_Design', max_length=500)  # Field name made lowercase.
    fecha_ejecucion = models.CharField(db_column='Fecha_Ejecucion', max_length=500)  # Field name made lowercase.
    fecha_estado = models.CharField(db_column='Fecha_Estado', max_length=500)  # Field name made lowercase.
    fecha_solicitud = models.CharField(db_column='Fecha_Solicitud', max_length=500)  # Field name made lowercase.
    hub = models.CharField(db_column='HUB', max_length=500, blank=True, null=True)  # Field name made lowercase.
    horas_90 = models.CharField(db_column='Horas_90', max_length=500)  # Field name made lowercase.
    horas_95 = models.CharField(db_column='Horas_95', max_length=500)  # Field name made lowercase.
    kpi_design = models.CharField(db_column='KPI_DESIGN', max_length=500)  # Field name made lowercase.
    kpi_ejecucion = models.CharField(db_column='KPI_EJECUCION', max_length=500)  # Field name made lowercase.
    mes_ejecucion = models.CharField(db_column='MES_Ejecucion', max_length=500)  # Field name made lowercase.
    mes = models.CharField(db_column='Mes', max_length=500)  # Field name made lowercase.
    mes_ejecucion_2 = models.CharField(db_column='Mes_Ejecucion_2', max_length=500)  # Field name made lowercase.
    mes_sol = models.CharField(db_column='Mes_Sol', max_length=500)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=500)  # Field name made lowercase.
    obs_solicitud = models.CharField(db_column='OBS_Solicitud', max_length=500)  # Field name made lowercase.
    obras_complementarias = models.CharField(db_column='Obras_Complementarias', max_length=500)  # Field name made lowercase.
    observaciones_capo = models.CharField(db_column='Observaciones_CaPO', max_length=500)  # Field name made lowercase.
    responsable = models.CharField(db_column='Responsable', max_length=500)  # Field name made lowercase.
    semana_ejecucion = models.CharField(db_column='Semana_Ejecucion', max_length=500)  # Field name made lowercase.
    sol2 = models.CharField(db_column='Sol2', max_length=500)  # Field name made lowercase.
    tipo_solucion = models.CharField(db_column='Tipo_Solucion', max_length=500)  # Field name made lowercase.
    tipo_de_red = models.CharField(db_column='Tipo_de_Red', max_length=500)  # Field name made lowercase.
    w_solicitud = models.CharField(db_column='W_Solicitud', max_length=500)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=500)  # Field name made lowercase.
    year_2022 = models.CharField(db_column='Year_2022', max_length=500)  # Field name made lowercase.
    year_ejecucion = models.CharField(db_column='Year_Ejecucion', max_length=500)  # Field name made lowercase.
    zona_roja = models.CharField(db_column='Zona_Roja', max_length=500)  # Field name made lowercase.
    id = models.AutoField(primary_key=True,db_column='id',blank=False,null=False)

    class Meta:
        managed = True
        db_table = 'capacidad'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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


class rollbackDB(models.Model):
    row_1 = models.CharField(db_column='row_1',max_length=500, default="")
    row_2 =	models.CharField(db_column='row_2',max_length=500, default="")
    row_3 =	models.CharField(db_column='row_3',max_length=500, default="")
    row_4 =	models.CharField(db_column='row_4', max_length=500, default="")
    Ups_Downs_Chan = models.CharField(db_column='Ups_Downs_Chan', max_length=500, default="")
    row_6 =	models.CharField(db_column='row_6',max_length=500, default="")
    row_7 =	models.CharField(db_column='row_7',max_length=500, default="")
    mac_cm = models.CharField(db_column='mac_cm', max_length=500, default="")
    Ip_Address = models.CharField(db_column='Ip_Address', max_length=500, default="")

    class Meta:
        managed = True
        db_table = 'rollbackDB'
