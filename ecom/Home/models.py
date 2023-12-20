from django.db import models

# Create your models here.

class Top_Banner_Images(models.Model):
    id = models.AutoField(primary_key=True)
    top_brand = models.CharField(max_length=100,null=True, blank=True)
    new_collection = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(max_length=500,null=True, blank=True)
    slider = models.ImageField(upload_to='productimg')
    def __str__(self):
        return str(self.id)
    
class Midel_40_Images(models.Model):
    id = models.AutoField(primary_key=True)
    new = models.CharField(max_length=100,null=True, blank=True)
    new_fashion = models.CharField(max_length=100,null=True, blank=True)
    description_40 = models.TextField(max_length=500,null=True, blank=True)
    image = models.ImageField(upload_to='productimg')
    def __str__(self):
        return str(self.id)
