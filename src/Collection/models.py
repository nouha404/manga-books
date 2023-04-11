from django.db import models
from django.utils.text import slugify

from GestionComptes.models import CustomUser

LECTURE_CHOIX = (
    ('non-lu', 'Non lu'),
    ('en-cours', 'En cours'),
    ('lu', 'Lu'),
)
GENRE_CHOICES = (
    ('action', 'Action'),
    ('aventure', 'Aventure'),
    ('comédie', 'Comédie'),
    ('drame', 'Drame'),
    ('ecchi', 'Ecchi'),
    ('fantaisie', 'Fantaisie'),
    ('horreur', 'Horreur'),
    ('mecha', 'Mecha'),
    ('romance', 'Romance'),
    ('science-fiction', 'Science-fiction'),
    ('slice-of-life', 'Slice of life'),
    ('sport', 'Sport'),
    ('yaoi', 'Yaoi'),
    ('yuri', 'Yuri'),
    ('shonen-ai', 'Shonen-ai'),
    ('shoujo-ai', 'Shoujo-ai'),
    ('magical-girl', 'Magical girl'),
    ('harem', 'Harem'),
    ('isekai', 'Isekai'),
    ('historique', 'Historique'),
    ('mystère', 'Mystère'),
    ('psychologique', 'Psychologique'),
    ('tranche-de-vie', 'Tranche de vie'),
)


class Gender(models.Model):
    name = models.CharField(blank=False, choices=GENRE_CHOICES, verbose_name="Genre", max_length=100)
    slug = models.SlugField(blank=True)


# Create your models here.
class MangaWiki(models.Model):
    collection_author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    author = models.CharField(blank=False, max_length=40, verbose_name="Auteur")
    number_of_volume = models.IntegerField(blank=False, unique=False, verbose_name="Nombre de volume")
    status = models.CharField(blank=False, choices=LECTURE_CHOIX, verbose_name="Etat de Lecture", max_length=100)
    note = models.TextField(max_length=25, blank=False)

    gender = models.ManyToManyField(Gender, blank=True)
    title = models.CharField(blank=False, max_length=60, verbose_name="Titre")
    slug = models.SlugField(blank=True)
    description = models.TextField(max_length=155, verbose_name="Description")

    class Meta:
        ordering = ['status']
        verbose_name = "Manga Collection"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
