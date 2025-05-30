from django.contrib import admin

from api.models import *


class ProduitsAdmin(admin.ModelAdmin):
    list_display = ("libelle", "prix", "quantite", "unite", "description", )
    list_editable = ("quantite",)
    list_display_links = ("libelle", )
    search_fields = ['libelle', 'quantite']
    list_filter = ("prix", "unite")
    list_per_page = 50


class CategorieAdmin(admin.ModelAdmin):
    list_display = ("id","nom", "type",)

    list_display_links = ("nom", )
    search_fields = ['type', ]
    list_filter = ("type", )
    list_per_page = 50


admin.site.register(Produits, ProduitsAdmin)
admin.site.register(Categorie, CategorieAdmin)