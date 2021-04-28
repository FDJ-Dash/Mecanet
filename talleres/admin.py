from django.contrib import admin

# Register your models here.
from .models import Talleres


#class TalleresAdmin(admin.ModelAdmin):

admin.site.register(Talleres)