from django.db import models
from Category.models import Categories
from SubCategory.models import SubCategories

STOCK_CHOICES = (
    ('SI', 'In Stock'),
    ('SO', 'Out Stock'),
  
)

    
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField(max_length=100)
    discount_price = models.FloatField(max_length=100)
    basi_description = models.TextField(max_length=100)
    details_description = models.TextField(max_length=100)
    brand = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    sub_cat_id = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    stock = models.CharField(choices= STOCK_CHOICES, max_length=40)
    product_1_image = models.ImageField(upload_to='productimg')
    product_2_image = models.ImageField(upload_to='productimg')
    product_3_image = models.ImageField(upload_to='productimg')
    product_4_image = models.ImageField(upload_to='productimg')
    
    def __str__(self):
        return str(self.id)



    