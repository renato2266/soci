from django.contrib import admin

# Register your models here.
from .models import Soci

class SociModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nome", "luogo", "data"]
    list_filter = ["data"]
    search_fields = ["cognome", "nome" , "data"]
    prepopulated_fields = {"slug": ("cognome",)}

    class Meta:
        model = Soci

admin.site.register(Soci, SociModelAdmin)
