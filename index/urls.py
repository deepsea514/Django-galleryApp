from django.urls import path,include
from .views import *
urlpatterns = [

  path('index', index, name='index'),
  path('gallery', gallery, name='gallery'),
  path('detail', product_detail, name='product-detail')
]
