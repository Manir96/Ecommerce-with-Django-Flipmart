from django.db import models
from Category.models import Categories

# Create your models here.

class SubCategories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    cat_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
