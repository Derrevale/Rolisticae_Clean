from django.contrib import admin
from .models import Categorie, Article

admin.site.register(Categorie)
admin.site.register(Article)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'slug')
    readonly_fields = ('slug',)