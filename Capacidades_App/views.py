from ast import Pass
from itertools import count
from traceback import print_list
from turtle import update
from django.shortcuts import render, redirect
from .models import AddressVTRDb, capacidad, rollbackDB, VTR_Roll_Model
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F
from .forms import capacidadForm
from django.contrib import messages
from tablib import Dataset
import csv
import io
import pandas as pd
import sqlalchemy

# Create your views here.
def index(request):
    book = capacidad.objects.all()
    context = {'book': book}
    return render(request, 'index.html', context)

def base(request):
    return render(request, 'base.html')

def dashboard(request):
    book = capacidad.objects.all().values().order_by("SGI_INDEX")
    p = Paginator(book, per_page=15)  # creating a paginator object
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, './dashboard.html', context)


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        multiple_post = Q(Q(SGI_INDEX__icontains=search) | Q(Zona__icontains=search) | Q(Estado_Ejecucion__icontains=search) | Q(Tipo_Solucion__icontains=search) | Q(Fecha_Ejecucion__icontains=search) | Q(
            EPS__icontains=search) | Q(Estado_CaPO__icontains=search) | Q(Clave__icontains=search))  # Aca podemos ejecutar los diferentes filtros que queramos aplicar a nuestra searchbar
        post = capacidad.objects.all().filter(multiple_post)
        context_2 = {'post': post}
        # sending the page object to index.html
        return render(request, './searchbar.html', context_2)


def crearCapacidad(request):
    if request.method == 'GET':
        form = capacidadForm()
        contexto = {'form': form}
    else:
        # Llamando a capacidadForm(request.POST) el cual contiene toda nuestra base al hacerle un request.POST me permite ingresar informacion en ella.
        form = capacidadForm(request.POST)
        contexto = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'crear_Capacidad.html', contexto)#Rompe el ciclo para entregar finalmente la URL con su contexto y pueda ser tomada finalmente por el motor de Django y ser trabajada por los demas archivos.
    # post = capacidad.objects.all().filter(ID_SGI__icontains=search)
    # return render(request,'./searchbar.html',{'post':post})


def editarCapacidad(request, SGI_INDEX):
    book = capacidad.objects.get(SGI_INDEX=SGI_INDEX)
    if request.method == 'GET':
        # Dentro de book se creara una instancia de una clase particular en este caso ID_SGI es el que se esta tomando en cuenta.
        form = capacidadForm(instance=book)
        contexto = {'form': form}
    else:
        form = capacidadForm(request.POST, instance=book)
        contexto = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, 'crear_Capacidad.html', contexto)

def eliminarCapacidad(request, SGI_INDEX):
    book = capacidad.objects.get(SGI_INDEX=SGI_INDEX)
    book.delete()
    return redirect('dashboard')

def profile_upload(request):
    # declaring template
    template = "upload.html"
    data = capacidad.objects.all().values()
    prompt = {
        'order': 'Order of the CSV should be: ID_SGI , Zona ...',
        'capacidades': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream.
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=','):
        created = capacidad.objects.update_or_create(Ano_Solicitud=column[0], SGI_INDEX=column[1], Zona=column[2], HUB=column[3], Comuna=column[4], Clave=column[5], Cuadrantes=column[6], Cantidad_N=column[7], Fecha_Solicitud=column[8], Year=column[9], Mes=column[10], W_Solicitud=column[11], OBS_Solicitud=column[12], Tipo_Solucion=column[13], Clientes_Afectados=column[14], Estado_Ejecucion=column[15], Sol2=column[16], Fecha_Cancelado=column[17], Tipo_de_Red=column[18], Estado_Design_Simplificado=column[19], Fecha_Design=column[20], Asignacion_Energía=column[21], Obras_Complementarias=column[
                                                     22], Estado_Asignación_Energía=column[23], Estado_Ejecucion_2=column[24], Fecha_Ejecucion=column[25], Year_Ejecucion=column[26], MES_Ejecucion=column[27], Semana_Ejecucion=column[28], EPS=column[29], Fecha_Comunicacion_EPS=column[30], Responsable=column[31], Motivo=column[32], KPI_DESIGN=column[33], KPI_EJECUCION=column[34], Estado_CaPO=column[35], Fecha_Estado=column[36], Observaciones_CaPO=column[37], Horas_95=column[38], Horas_90=column[39], Zona_Roja=column[41], Clase_Zona_Roja=column[41], Mes_Sol=column[42], Mes_Ejecucion_2=column[43], Year_2022=column[44],)
    return redirect('dashboard')

def rollback_from_csv(request):
    # declaring template
    template = "upload-rb.html"
    data = rollbackDB.objects.all().values('row_1','row_2','row_3','row_4','Ups_Downs_Chan','row_6','row_7','mac_cm','Ip_Address')
    prompt = {
        'order': 'Order of the CSV should be: row_1 , row_2 ...',
        'rollbackDB': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    


    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream.
    io_string = io.StringIO(data_set)   
    
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=','):
        created = rollbackDB.objects.all().update_or_create(row_1=column[0],row_2=column[1],row_3=column[2],row_4=column[3],Ups_Downs_Chan=[4],row_6=column[5],row_7=column[6],mac_cm=column[7],Ip_Address=column[8])
    return redirect('rollback_upload')

def rollback_upload(request):
    capacidadDB = pd.DataFrame(list(capacidad.objects.all().values("Comuna","Clave","Cuadrantes","Tipo_Solucion","SGI_INDEX")))#De esta forma podemos invocar un dataframe copiando las exactas columnas desde un Model.
    capacidadDB["Clave"] = capacidadDB["Clave"].map(lambda x: x[4:])#Corta todo el nombre de la clave y solo deja el numero del nodo.
    capacidadDB["Clave"] = capacidadDB["Clave"].astype(str).str.zfill(3)
    capacidadDB["Cuadrantes"] = capacidadDB["Cuadrantes"].map(lambda x: x[1:])#.astype(str).str.zfill(3)
   
   #SEGUIR PROBANDO ESTO MAÑANA.
    #capacidadDB[["Q1","Q2","Q3"]]=capacidadDB["Clave"].str.split("Q",expand=True)
    
    
    print(capacidadDB.to_string())
    capacidadDB["Q1"] = capacidadDB["Cuadrantes"].str.slice(start=0, stop=1).astype(str).str.zfill(3)#Todos los que poseen mas de 1Q estaran aca
    capacidadDB["Q1"] = capacidadDB["Cuadrantes"].str.slice(start=2, stop=3).astype(str).str.zfill(3)#Todos los que poseen solo 1Q estaran aca
    capacidadDB_2 = capacidadDB.query("Tipo_Solucion == 'GO 85'")
    #print(capacidadDB_2.to_string())
    last_df_Q1 = capacidadDB_2[['Comuna','Clave','Tipo_Solucion','Q1','SGI_INDEX']].copy()
    last_df_Q2 = capacidadDB_2[['Comuna','Clave','Tipo_Solucion','Q1','SGI_INDEX']].copy()
    total_last_df = last_df_Q1.append(last_df_Q2, ignore_index = True) #THIS!
    total_last_df["nodo_cuadrante"] = total_last_df['Comuna']+total_last_df['Clave'] + total_last_df['Q1']
    
    moving_SGI_INDEX = total_last_df.pop('SGI_INDEX')
    total_last_df.insert(5, 'SGI_INDEX', moving_SGI_INDEX)
    total_last_df_T = pd.DataFrame(total_last_df)
    
    ###################################################################################################
        #print(capacidadDB_2)
    #capacidadDB_2['new_column_name'] = capacidadDB["Comuna"] + capacidadDB["Clave"] + capacidadDB["Cuadrantes"]
    #VTR_Roll_Model_DB = pd.DataFrame(list(VTR_Roll_Model.objects.all().values()))
    
    #df3 = capacidadDB_2.concat([df1, df2], ignore_index = True) #THIS!
    macAdd_rollbackDB = rollbackDB.objects.all().values("mac_cm").distinct()
    macAdd_AddressVTRDb = AddressVTRDb.objects.all().values("mac_cm")
    macDir_AddressVTRDb = AddressVTRDb.objects.all().values("nom_direc")
    macAdd_Roll= pd.DataFrame(list(rollbackDB.objects.all().values("mac_cm")))#.distinct
    #-->
    macDir_NodoCodLoca = pd.DataFrame(list(AddressVTRDb.objects.all().values("mac_cm","nom_direc","cod_loca","cod_nodo","cod_cuadrante","num_latit","num_longit")))
    
    dict_dframe_merger = pd.merge(macAdd_Roll, macDir_NodoCodLoca, on=["mac_cm", "mac_cm"])#Nombres de las columnas en OJO: "EXCEL"
        
    df = pd.DataFrame(dict_dframe_merger)
    
    df["cod_nodo"] = df["cod_nodo"].astype(str).str.zfill(3)
    df["cod_cuadrante"] = df["cod_cuadrante"].astype(str).str.zfill(3)
    df["nodo_cuadrante"] = df["cod_loca"] + df["cod_nodo"] + df["cod_cuadrante"]
    df_2 = pd.DataFrame(df)
    #print(df_2)
    
    
    dict_dframe_merger_2 = pd.merge(total_last_df_T,df_2,on="nodo_cuadrante" )
    print(dict_dframe_merger_2)
    
    
    #print(dict_dframe_merger_2)
    df_3 = pd.DataFrame(dict_dframe_merger_2)
    
    df_3.drop_duplicates(subset =["mac_cm"],inplace=True)
    
    df_definitivo_cruzado = df_3[["mac_cm","nom_direc","cod_loca","cod_nodo","cod_cuadrante","num_latit","num_longit","nodo_cuadrante","SGI_INDEX"]].copy()

    #df_definitivo_cruzado = df_definitivo_cruzado.query("nodo_cuadrante == 'VINA055002'") 
    #print(df_definitivo_cruzado)
    
    dbEngine=sqlalchemy.create_engine('sqlite:///db.sqlite3')#,options: echo=True     # ensure this is the correct path for the sqlite file. 
    
    sqlite_connection = dbEngine.connect()
    sqlite_table = 'VTR_Roll_Model'
    df_definitivo_cruzado.to_sql(sqlite_table, sqlite_connection, if_exists='replace')
    sqlite_connection.close()
    
    #capacidadDB["Clave"] = capacidadDB["Clave"].str.slice(start=5, stop=6) #THIS IS IT! for slicing index.

    #capacidadDB = capacidadDB.query("Tipo_Solucion == 'GO 85'") 

    #list_macAdd_rollbackDB = []
    #list_macAdd_AddressVTRDb = []
    #list_macDir_AddressVTRDb = []
    #list_macDir_Nodo_C_Lat = []

            
    #for a in macAdd_rollbackDB:
    #    list_macAdd_rollbackDB.append( a['mac_cm'] ) 
        
    #for a in macAdd_AddressVTRDb:
    #    list_macAdd_AddressVTRDb.append( a['mac_cm'] )

    #for b in macDir_AddressVTRDb:
    #    list_macDir_AddressVTRDb.append( b['nom_direc'] )
    
    #1 dict_1_dframe = pd.DataFrame({'mac_cm':list_macAdd_rollbackDB})
    #2 dict_2_dframe = pd.DataFrame({'mac_cm':list_macAdd_AddressVTRDb,'nom_direc':list_macDir_AddressVTRDb, 'cod_loca':macDir_NodoCodLoca["cod_loca"]})
    #3 print(dict_2_dframe)
    
    #4 dict_dframe_merger = pd.merge(dict_1_dframe, dict_2_dframe, on=["mac_cm", "mac_cm"])#Nombres de las columnas en OJO: "EXCEL"
    #5 df = pd.DataFrame(dict_dframe_merger)
    
    #print(dict_dframe_merger)
    #print(df) #IT WORKED, convirtio el DICT a formato SQL para poder enviarlo asi a la DB.
    

#2.-Turn on database engine
    # 5 df.to_sql(sqlite_table, sqlite_connection, if_exists='replace')
    return render(request,'rollback_upload_warning.html')#7 {'data':new_object}

def rollback_tab(request):
    new_object = VTR_Roll_Model.objects.all()
    new_object = VTR_Roll_Model.objects.all().values("mac_cm","nom_direc","cod_loca","cod_nodo","cod_cuadrante","num_latit","num_longit","SGI_INDEX").order_by('nom_direc')
    p = Paginator(new_object, per_page=20)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'page_obj': page_obj,'data':new_object}
   
#    capacidadDB = pd.DataFrame(list(capacidad.objects.all().values("Comuna","Clave","Cuadrantes","Tipo_Solucion")))#De esta forma podemos invocar un dataframe copiando las exactas columnas desde un Model.
    
    #capacidadDB["Clave"] = capacidadDB["Clave"].str.slice(start=5, stop=6) #THIS IS IT! for slicing index.
#    capacidadDB["Clave"] = capacidadDB["Clave"].map(lambda x: x[4:]) #+ capacidadDB["Clave"].map(lambda x: x[4:])
#    capacidadDB["Clave"] = capacidadDB["Clave"].astype(str).str.zfill(3) # Para rellenar toda la columna con un indice de numeros predeterminado en este caso colocara hasta 3 0 de no haber nada en la columna, de haber 1 solo numero colocara 2 ceros, de haber 2 numberos colocara 1 solo 0.
#    capacidadDB["Cuadrantes"] = capacidadDB["Cuadrantes"].map(lambda x: x[1:]).astype(str).str.zfill(3) #Podemos ubicar mapeando la columna hasta el indice predeterminado en este caso comienza a mostrar los valores luego del 5 indice inclusivo.
                                                                                                        #En este caso lo hicimos todo en una sola linea de codigo.
    #capacidadDB = capacidadDB.query("Tipo_Solucion == 'GO 85'") 
#    value = 'GO 85'
#    capacidadDB.loc[capacidadDB['Tipo_Solucion'] == value]
#    print(capacidadDB)
    
    #new = capacidadDB["Cuadrantes"].copy() #Copia la columna de la base de datos.
    
    #capacidadDB["Cuadrantes"].str.cat(new,sep ="00") #Para concatenar Cadenas a toda la columna
    #capacidadDB["Cuadrantes"] = capacidadDB["Cuadrantes"].str.slice(start=1, stop=2) #Corta desde un indice hasta otro indice
    
    
    #capacidadDB["Cuadrantes"] = capacidadDB["Cuadrantes"].map(lambda x: x[1:])
    #capacidadDB["Cuadrantes"] = capacidadDB["Cuadrantes"].astype(int)
    #new = capacidadDB["Cuadrantes"].copy()
    #capacidadDB["Cuadrantes"] = capacidadDB["Cuadrantes"].str.cat(new, sep ="00")
    #capacidadDB["Cuadrantes"] = capacidadDB["Cuadrantes"].astype(int)
    #capacidadDB["Cuadrantes"] = capacidadDB["Cuadrantes"].map(lambda x: x[1:])
    
    
    #capacidadDB[pd.to_numeric(capacidadDB.Cuadrantes, 'coerce').gt(9)] # PARA GREATHERS THAN CERTAIN NUMBERS.
    
    
    
    #print(capacidadDB)
    
    """_summary_
            macAdd_rollbackDB = rollbackDB.objects.all().values("mac_cm").distinct()
            macAdd_AddressVTRDb = AddresTsVRDb.objects.all().values("mac_cm")
            macDir_AddressVTRDb = AddressVTRDb.objects.all().values("nom_direc")
            macAdd_Roll= pd.DataFrame(list(rollbackDB.objects.all().values("mac_cm").distinct()))
            macDir_NodoCodLoca = pd.DataFrame(list(AddressVTRDb.objects.all().values("mac_cm","nom_direc","cod_loca","cod_nodo","cod_cuadrante","num_latit","num_longit")))
            dict_dframe_merger = pd.merge(macAdd_Roll, macDir_NodoCodLoca, on=["mac_cm", "mac_cm"])#Nombres de las columnas en OJO: "EXCEL"
            df = pd.DataFrame(dict_dframe_merger)
            dbEngine=sqlalchemy.create_engine('sqlite:///db.sqlite3')#,options: echo=True     # ensure this is the correct path for the sqlite file. 
            
            sqlite_connection = dbEngine.connect()
            sqlite_table = 'VTR_Roll_Model'
            df.to_sql(sqlite_table, sqlite_connection, if_exists='replace')
            sqlite_connection.close()
            
            macAdd_rollbackDB = rollbackDB.objects.all().values("mac_cm").distinct()
    """
    
    """
    capacidadDB = pd.DataFrame(list(capacidad.objects.all().values("Comuna","Clave","Cuadrantes","Tipo_Solucion","SGI_INDEX")))#De esta forma podemos invocar un dataframe copiando las exactas columnas desde un Model.
    capacidadDB["Clave"] = capacidadDB["Clave"].map(lambda x: x[4:])
    capacidadDB["Clave"] = capacidadDB["Clave"].astype(str).str.zfill(3)
    capacidadDB["Cuadrantes"] = capacidadDB["Cuadrantes"].map(lambda x: x[1:]).astype(str).str.zfill(3)
    value = 'GO 85'
    capacidadDB["Q1"] = capacidadDB["Cuadrantes"].str.slice(start=0, stop=1).astype(str).str.zfill(3)#Todos los que poseen mas de 1Q estaran aca
    capacidadDB["Q1"] = capacidadDB["Cuadrantes"].str.slice(start=2, stop=3).astype(str).str.zfill(3)#Todos los que poseen solo 1Q estaran aca.
    
    

    capacidadDB_2 = capacidadDB.query("Tipo_Solucion == 'GO 85'")
    #capacidadDB_2['new_column_name'] = capacidadDB["Comuna"] + capacidadDB["Clave"] + capacidadDB["Cuadrantes"]
    #VTR_Roll_Model_DB = pd.DataFrame(list(VTR_Roll_Model.objects.all().values()))
    
    #df3 = capacidadDB_2.concat([df1, df2], ignore_index = True) #THIS!
    last_df_Q1 = capacidadDB_2[['Comuna','Clave','Tipo_Solucion','Q1','SGI_INDEX']].copy()
    last_df_Q2 = capacidadDB_2[['Comuna','Clave','Tipo_Solucion','Q1','SGI_INDEX']].copy()
    total_last_df = last_df_Q1.append(last_df_Q2, ignore_index = True) #THIS!
    total_last_df["nodo_cuadrante"] = capacidadDB['Comuna']+capacidadDB['Clave'] + capacidadDB['Q1']
    
    print(total_last_df)
    """
    
    return render(request,'rollback_tab.html',context)#7 {'data':new_object}