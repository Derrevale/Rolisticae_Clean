from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField  # Pour le texte enrichi

class Categorie(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre

class Article(models.Model):
    titre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/')
    description = RichTextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(default=timezone.now)
    publie = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
