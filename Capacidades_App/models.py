from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class capacidad(models.Model):
    
    Ano_Solicitud = models.CharField(
        blank=True, null=True, max_length=500, default="")
    SGI_INDEX = models.CharField(
        null=True, max_length=500, unique=True, default="")
    Zona = models.CharField(blank=True, null=True, max_length=500, default="")
    HUB = models.CharField(blank=True, null=True, max_length=500, default="")
    Comuna = models.CharField(blank=True, null=True, max_length=500)
    Clave = models.CharField(blank=True, max_length=500, default="")
    Cuadrantes = models.CharField(blank=True, max_length=500, default="")
    Cantidad_N = models.CharField(blank=True, max_length=500, default="")
    Fecha_Solicitud = models.CharField(blank=True, max_length=500, default="")
    Year = models.CharField(blank=True, max_length=500, default="")
    Mes = models.CharField(blank=True, max_length=500, default="")
    W_Solicitud = models.CharField(blank=True, max_length=500, default="")
    OBS_Solicitud = models.CharField(
        blank=True, null=False, max_length=500, default="")
    Tipo_Solucion = models.CharField(blank=True, max_length=500, default="")
    Clientes_Afectados = models.CharField(
        blank=True, max_length=500, default="")
    Estado_Ejecucion = models.CharField(blank=True, max_length=500, default="")
    Sol2 = models.CharField(blank=True, max_length=500, default="")
    Fecha_Cancelado = models.CharField(max_length=500, default="")
    Tipo_de_Red = models.CharField(blank=True, max_length=500, default="")
    Estado_Design_Simplificado = models.CharField(
        blank=True, max_length=500, default="")
    Fecha_Design = models.CharField(blank=True, max_length=500, default="")
    Asignacion_Energía = models.CharField(
        blank=True, max_length=500, default="")
    Obras_Complementarias = models.CharField(
        blank=True, max_length=500, default="")
    Estado_Asignación_Energía = models.CharField(
        blank=True, max_length=500, default="")
    Estado_Ejecucion_2 = models.CharField(
        blank=True, max_length=500, default="")
    Fecha_Ejecucion = models.CharField(blank=True, max_length=500, default="")
    Year_Ejecucion = models.CharField(blank=True, max_length=500, default="")
    MES_Ejecucion = models.CharField(blank=True, max_length=500, default="")
    Semana_Ejecucion = models.CharField(blank=True, max_length=500, default="")
    EPS = models.CharField(blank=True, max_length=500, default="")
    Fecha_Comunicacion_EPS = models.CharField(
        blank=True, max_length=500, default="")
    Responsable = models.CharField(blank=True, max_length=500, default="")
    Motivo = models.CharField(blank=True, max_length=500, default="")
    KPI_DESIGN = models.CharField(blank=True, max_length=500, default="")
    KPI_EJECUCION = models.CharField(blank=True, max_length=500, default="")
    Estado_CaPO = models.CharField(blank=True, max_length=500, default="")
    Fecha_Estado = models.CharField(blank=True, max_length=500, default="")
    Observaciones_CaPO = models.CharField(
        blank=True, max_length=500, default="")
    Horas_95 = models.CharField(blank=True, max_length=500, default="")
    Horas_90 = models.CharField(blank=True, max_length=500, default="")
    Zona_Roja = models.CharField(blank=True, max_length=500, default="")
    Clase_Zona_Roja = models.CharField(blank=True, max_length=500, default="")
    Mes_Sol = models.CharField(blank=True, max_length=500, default="")
    Mes_Ejecucion_2 = models.CharField(blank=True, max_length=500, default="")
    Year_2022 = models.CharField(blank=True, max_length=500, default="")
    #id = models.AutoField(primary_key=True,db_column='id',blank=False,default="")
    #id = models.AutoField(primary_key=True,db_column='id',blank=False,default="")

    class Meta:
        managed = True
        db_table = 'capacidad'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
        
class AddressVTRDb(models.Model):
    iden_vivienda_gis = models.IntegerField(db_column='IDEN_VIVIENDA_GIS', blank=True, null=True)  # Field name made lowercase.
    mac_cm = models.TextField(db_column='MAC_CM', blank=True, null=True)  # Field name made lowercase.
    nom_direc = models.TextField(db_column='NOM_DIREC', blank=True, null=True)  # Field name made lowercase.
    cod_loca = models.TextField(db_column='COD_LOCA', blank=True, null=True)  # Field name made lowercase.
    cod_nodo = models.IntegerField(db_column='COD_NODO', blank=True, null=True)  # Field name made lowercase.
    cod_cuadrante = models.IntegerField(db_column='COD_CUADRANTE', blank=True, null=True)  # Field name made lowercase.
    num_latit = models.FloatField(db_column='NUM_LATIT', blank=True, null=True)  # Field name made lowercase.
    num_longit = models.FloatField(db_column='NUM_LONGIT', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True,db_column='id',blank=False,default="")
    #cod_loca,cod_nodo,cod_cuadrante,num_latit,num_longit
    #rollbackdb = models.ForeignKey(rollbackDB,on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        db_table = 'AddressVTRDb'

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
#    addressvtr = models.ForeignKey(AddressVTRDb,on_delete=models.CASCADE, null=True, blank=True)
#    id = models.AutoField(primary_key=True,db_column='id',blank=False,default="")
    
    class Meta:
        db_table = 'rollbackDB'
        
class VTR_Roll_Model(models.Model): 
    mac_cm = models.TextField(db_column='mac_cm', blank=True, null=True)
    nom_direc = models.TextField(db_column='nom_direc', blank=True, null=True)  # Field name made lowercase.
    cod_loca = models.TextField(db_column='COD_LOCA', blank=True, null=True)  # New Field
    cod_nodo = models.IntegerField(db_column='COD_NODO', blank=True, null=True)  # New Field
    cod_cuadrante = models.IntegerField(db_column='COD_CUADRANTE', blank=True, null=True)  # New Field
    num_latit = models.FloatField(db_column='NUM_LATIT', blank=True, null=True)  # New Field
    num_longit = models.FloatField(db_column='NUM_LONGIT', blank=True, null=True)  # New Field
    nodo_cuadrante = models.TextField(db_column='nodo_cuadrante', blank=True, null=True)  # New Field
    SGI_INDEX = models.CharField(db_column='SGI_INDEX', null=True, max_length=500, unique=True, default="") 
    created_at = models.DateTimeField(db_column='created_at',auto_now_add=True)
    id = models.AutoField(primary_key=True,db_column='id',blank=False,default="")#PROBAR SIN ESTE FIELD
    
    class Meta:
        db_table = 'VTR_Roll_Model'