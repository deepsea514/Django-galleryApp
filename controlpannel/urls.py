from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('controlpannel', control_pannel, name='controlPannel'),
    path('test', test)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)