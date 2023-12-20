from django.contrib import admin
from .models import DataSet,WeightNN,BiasNN,FraudScore,Log


class LogAdmin(admin.ModelAdmin):
    list_display = ["id","EventDT","log"]
    fields = ["id","EventDT","log"]
    
admin.site.register(DataSet)
admin.site.register(WeightNN)
admin.site.register(BiasNN)
admin.site.register(FraudScore)
admin.site.register(Log, LogAdmin)

# Register your models here.
