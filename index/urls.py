from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  path('', index, name='index'),
  path('gallery', gallery, name='gallery'),
  path('detail/<int:key_id>', product_detail, name='product-detail'),
  path('productdetail/<int:key_id>', product_side_images, name='productdetail')
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
