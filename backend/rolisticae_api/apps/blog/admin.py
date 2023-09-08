from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'publie_check')

    def publie_check(self, obj):
        return '✅' if obj.publie else '❌'

    publie_check.short_description = 'Publié'
    publie_check.allow_tags = True

    actions = ['mark_as_published', 'mark_as_unpublished']

    def mark_as_published(self, request, queryset):
        queryset.update(publie=True)

    mark_as_published.short_description = "Marquer comme publié"

    def mark_as_unpublished(self, request, queryset):
        queryset.update(publie=False)

    mark_as_unpublished.short_description = "Marquer comme non publié"


admin.site.register(Article, ArticleAdmin)
