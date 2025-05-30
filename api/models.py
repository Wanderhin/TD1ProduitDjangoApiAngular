from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    type = models.CharField(max_length=30)


class Produits(models.Model):
    libelle = models.CharField(max_length=30, verbose_name="libelle")
    prix = models.FloatField()
    quantite = models.FloatField()
    unite = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)


