import os

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField  # Pour le texte enrichi
from django.dispatch import receiver


class Categorie(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.titre}-slug")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre


class Article(models.Model):
    titre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/')
    description = RichTextUploadingField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(default=timezone.now)
    publie = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, related_name='articles', on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

@receiver(post_delete, sender=Article)
def article_post_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(pre_save, sender=Article)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        old_instance = Article.objects.get(pk=instance.pk)
        old_image = old_instance.image
        new_image = instance.image
        if old_image != new_image:
            if os.path.isfile(old_image.path):
                os.remove(old_image.path)