from rest_framework import viewsets
from .models import Article, Categorie
from .serializers import ArticleSerializer, CategorieSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-date_publication')
    serializer_class = ArticleSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer