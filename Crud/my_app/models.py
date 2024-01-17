from django.db import models

# Create your models here.


class Article(models.Model):
    titre= models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self) -> str:
        return self.titre
