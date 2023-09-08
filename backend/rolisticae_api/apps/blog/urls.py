# blog/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Créer un routeur et enregistrer nos viewsets avec lui.
router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'categories', views.CategorieViewSet)

# Les URLs de l'API sont déterminées automatiquement par le routeur.
urlpatterns = [
    path('', include(router.urls)),
]
