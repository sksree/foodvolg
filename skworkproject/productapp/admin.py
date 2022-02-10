from django.contrib import admin
from . models import *

# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(categ,catadmin)

class proadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,proadmin)

