from django.db import models
from django.contrib.auth.hashers import check_password 

# Create your models here.
class user_register(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    identy_no = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    v_key = models.CharField(max_length = 500,default=0, unique=True)
    v_status = models.CharField(max_length = 500, default=0)
    
    