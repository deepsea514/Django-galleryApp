from django.db import models
from authorization.models import User
from datetime import datetime
# Create your models here.

class Categories(models.Model):
    category = models.CharField(primary_key=True, max_length=100)

class Product(models.Model):
    P_id = models.AutoField(primary_key= True)
    P_image = models.ImageField(upload_to='products/')
    P_price = models.IntegerField(default=0)
    P_name = models.CharField(max_length=50, default='temp')
    P_description = models.CharField(max_length=200, default='temp')
    P_category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

class Comments(models.Model):
    comment = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    P_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now(),null=True)

