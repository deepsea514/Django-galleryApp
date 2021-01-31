from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

  path('index', index, name='index'),
  path('gallery', gallery, name='gallery'),
  path('detail', product_detail, name='product-detail')
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
