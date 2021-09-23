from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name','species','breed','age','sex','get_vaccinations']

    def get_vaccinations(self,obj):
        return "\n".join([Vaccine.name for Vaccine in obj.vaccinations.all()])


admin.site.register(Vaccine)