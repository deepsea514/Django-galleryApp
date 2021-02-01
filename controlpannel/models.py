from django.db import models
from authorization.models import User
# Create your models here.
class Product(models.Model):
    P_id = models.AutoField(primary_key= True)
    P_image = models.ImageField(upload_to='products/')

class Comments(models.Model):
    comment = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    P_id = models.ForeignKey(Product, on_delete=models.CASCADE)
