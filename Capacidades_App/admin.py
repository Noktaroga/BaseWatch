from django.contrib import admin
from .models import capacidad, Profile, rollbackDB,AddressVTRDb
from import_export.admin import ImportExportModelAdmin
from django import forms

# Register your models here.
#admin.site.register(capacidad)
@admin.register(capacidad)
@admin.register(Profile)
@admin.register(rollbackDB)
@admin.register(AddressVTRDb)

class userdat(ImportExportModelAdmin):
    pass
