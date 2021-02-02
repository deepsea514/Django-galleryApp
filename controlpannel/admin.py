from django.contrib import admin
from .models import Product, Comments, Categories, Product_Side_Images
# Register your models here.

admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Categories)
admin.site.register(Product_Side_Images)
