from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('searchbar', views.searchbar, name='searchbar'),
    path('editar_Capacidad/<int:SGI_INDEX>',views.editarCapacidad, name='editar_Capacidad'),
    path('crear_Capacidad/', views.crearCapacidad, name='crear_Capacidad'),
    path('eliminar_Capacidad/<int:SGI_INDEX>',views.eliminarCapacidad, name='eliminar_Capacidad'),
    path('upload-csv/', views.profile_upload, name="profile_upload"),
    path('rollback_upload_DB',views.rollback_upload,name="rollback_upload"),
    path('rollback_tab',views.rollback_tab,name="rollback_tab"),
    path('upload-rollback/', views.rollback_from_csv, name="rollback_from_csv"),
]
