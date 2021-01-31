from django.db import models

# Create your models here.
class Product(models.Model):
    P_id = models.AutoField(primary_key= True)
    P_image = models.ImageField(upload_to='products/')