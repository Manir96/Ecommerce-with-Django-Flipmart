from django.db import models

# Create your models here.

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, unique=True)
