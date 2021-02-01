from django.contrib import admin
from .models import Product, Comments, Categories
# Register your models here.

admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Categories)
