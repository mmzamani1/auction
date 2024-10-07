from django.db import models

class Item(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200)
    